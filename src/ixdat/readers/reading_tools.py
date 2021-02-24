"""Module with possibly general-use tools for readers"""

from pathlib import Path
import time
import urllib.request
from ..config import CFG


STANDARD_TIMESTAMP_FORM = "%m/%d/%Y %H:%M:%S"


def timestamp_string_to_tstamp(
    timestamp_string,
    form=None,
    forms=(STANDARD_TIMESTAMP_FORM,),
):
    """Return the unix timestamp as a float by parsing timestamp_string

    Args:
        timestamp_string (str): The timestamp as read in the .mpt file
        form (str): The format string used by time.strptime (string-parse time). This is
            optional and overrides `forms` if given.
        forms (list of str): The formats you want to try for time.strptime, defaults to
            the standard timestamp form.
    """
    if form:
        forms = (form,)
    struct = None
    for form in forms:
        try:
            struct = time.strptime(timestamp_string, form)
            continue
        except ValueError:
            continue

    tstamp = time.mktime(struct)
    return tstamp


def prompt_for_tstamp(path_to_file, default="creation", form=STANDARD_TIMESTAMP_FORM):
    """Return the tstamp resulting from a prompt to enter a timestamp, or a default

    Args:
        path_to_file (Path): The file of the measurement that we're getting a tstamp for
        default (str or float): What to use as the tstamp if the user does not enter one.
            This can be a tstamp as a float, or "creation" to use the file creation time,
            or "now" to use `time.time()`.
        form (str): The specification string for the timestamp format. Defaults to
            `ixdat.readers.reading_tools.STANDARD_TIMESTAMP_FORM`
    """
    path_to_file = Path(path_to_file)

    if default == "creation":
        default_tstamp = path_to_file.stat().st_mtime
    elif default == "now":
        default_tstamp = time.time()
    elif type(default) in (int, float):
        default_tstamp = default
    else:
        raise TypeError("`default` must be a number or 'creation' or 'now'.")
    default_timestring = time.strftime(form, time.localtime(default_tstamp))

    tstamp = None
    timestamp_string = "Try at least once."
    while timestamp_string:
        timestamp_string = input(
            f"Please input the timestamp for the measurement at {path_to_file}.\n"
            f"Please use the format {form}.\n"
            f"Enter nothing to use the default default,"
            f" '{default}', which is '{default_timestring}'."
        )
        if timestamp_string:
            try:
                tstamp = time.mktime(time.strptime(timestamp_string, form))
            except ValueError:
                print(
                    f"Could not parse '{timestamp_string}' according as '{form}'.\n"
                    f"Try again or enter nothing to use the default."
                )
            else:
                break
    return tstamp or default_tstamp


def url_to_file(url, file_name="temp", directory=None):
    """Copy the contents of the url to a temporary file and return that file's Path."""
    directory = directory or CFG.ixdat_temp_dir
    suffix = "." + str(url).split(".")[-1]
    path_to_file = (directory / file_name).with_suffix(suffix)
    urllib.request.urlretrieve(url, path_to_file)
    return path_to_file