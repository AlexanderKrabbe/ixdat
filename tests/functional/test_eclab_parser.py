"""
The module tests correct parsing of a mpt files generated by the EC-lab
with use of the Zilien. The dataset with the files exists as
the 'ixdat-large-test-files' submodule.

NOTE: Test of PEIS technique is skipped, because the Ixdat does not support it.

"""
from pathlib import Path

from ixdat import Measurement

from pytest import approx, fixture, mark


DATA_DIR = Path(__file__).parent.parent.parent / "submodules/ixdat-large-test-files/"

"""
Data to use in the test.

Format is:

filename_with_technique: {
  "column_name": ("unit", (first_column_value, last_column_value)),
  ...
}
"""
TEST_DATA = {
    # MULTI-TECHNIQUE DATASET
    "biologic_multiple_techniques_dataset/multiple_techniques_dataset_01_02_CVA_C01.mpt": {  # noqa: E501
        "mode": ("", (2, 2)),
        "ox/red": ("red", (0, 1)),
        "error": ("", (0, 0)),
        "control changes": ("", (0, 0)),
        "Ns changes": ("", (0, 0)),
        "counter inc.": ("", (0, 0)),
        "time/s": ("s", (2.868160128949967e001, 5.592763878855476e002)),
        "control/V": ("V", (9.1791922e-001, 8.9992851e-001)),
        "Ewe/V": ("V", (9.1770262e-001, 9.0080881e-001)),
        "<I>/mA": ("mA", (-4.376391007099301e-004, 1.126740008349650e-002)),
        "cycle number": ("", (1.000000000000000e000, 6.000000000000000e000)),
        "(Q-Qo)/C": ("C", (0.0000000e000, 1.4638975e-003)),
        "I Range": ("", (41, 41)),
        "Rcmp/Ohm": ("Ohm", (0.0000000e000, 0.0000000e000)),
        "P/W": ("W", (-4.0162254e-007, 1.0149774e-005)),
        "Ns=0": ("", (0, 0)),  # this is automatically added by ixdat as a ConstantValue
    },
    "biologic_multiple_techniques_dataset/multiple_techniques_dataset_01_03_CP_C01.mpt": {  # noqa: E501
        "mode": ("", (1, 1)),
        "ox/red": ("red", (1, 0)),
        "error": ("", (0, 0)),
        "control changes": ("", (1, 1)),
        "Ns changes": ("", (0, 0)),
        "counter inc.": ("", (0, 0)),
        "Ns": ("", (0, 2)),
        "time/s": ("s", (5.602763878602855e002, 5.893783871251071e002)),
        "control/mA": ("mA", (0.0000000e000, -2.0000001e-003)),
        "<Ewe>/V": ("V", (8.8483948e-001, 8.2798851e-001)),
        "I/mA": ("mA", (1.2781935e-006, -2.0001377e-003)),
        "dQ/C": ("C", (7.1232675e-010, -1.9990615e-005)),
        "(Q-Qo)/C": ("C", (7.1232675e-010, 5.0315875e-006)),
        "half cycle": ("", (0, 1)),
        "Q charge/discharge/mA.h": (
            "mA.h",
            (1.978685425384362e-010, -5.552948449702752e-006),
        ),
        "I Range": ("", (42, 42)),
        "Rcmp/Ohm": ("Ohm", (0.0000000e000, 0.0000000e000)),
        "Energy charge/W.h": ("W.h", (1.750818973293703e-013, 6.555031900229182e-009)),
        "Energy discharge/W.h": (
            "W.h",
            (0.000000000000000e000, -4.919033634676710e-009),
        ),
        "Capacitance charge/µF": ("µF", (0.000000000000000e000, 2.273762151181344e002)),
        "Capacitance discharge/µF": (
            "µF",
            (0.000000000000000e000, 1.369492186275801e002),
        ),
        "Q discharge/mA.h": ("mA.h", (0.000000000000000e000, 5.552948449702752e-006)),
        "Q charge/mA.h": ("mA.h", (1.978685425384362e-010, 0.000000000000000e000)),
        "Capacity/mA.h": ("mA.h", (1.978685425384362e-010, 5.552948449702752e-006)),
        "Efficiency/%": ("%", (0.0000000e000, 7.9891510e001)),
        "cycle number": ("", (0.000000000000000e000, 0.000000000000000e000)),
        "P/W": ("W", (1.1309961e-009, -1.6560911e-006)),
    },
    "biologic_multiple_techniques_dataset/multiple_techniques_dataset_01_04_CP_C01.mpt": {  # noqa: E501
        "mode": ("", (1, 1)),
        "ox/red": ("red", (0, 0)),
        "error": ("", (0, 0)),
        "control changes": ("", (0, 0)),
        "Ns changes": ("", (0, 0)),
        "counter inc.": ("", (0, 0)),
        "Ns": ("", (0, 0)),
        "time/s": ("s", (5.894805871225253e002, 5.994803868699091e002)),
        "control/mA": ("mA", (-2.0000001e-003, -2.0000001e-003)),
        "Ewe/V": ("V", (8.2613617e-001, 6.2719619e-001)),
        "I/mA": ("mA", (-1.9717729e-003, -1.9393268e-003)),
        "dQ/C": ("C", (0.0000000e000, -1.9855208e-005)),
        "(Q-Qo)/C": ("C", (0.0000000e000, -1.9855208e-005)),
        "half cycle": ("", (0, 0)),
        "Q charge/discharge/mA.h": (
            "mA.h",
            (0.000000000000000e000, -5.515335538398682e-006),
        ),
        "I Range": ("", (41, 41)),
        "Rcmp/Ohm": ("Ohm", (0.0000000e000, 0.0000000e000)),
        "Energy charge/W.h": ("W.h", (0.000000000000000e000, 0.000000000000000e000)),
        "Energy discharge/W.h": (
            "W.h",
            (0.000000000000000e000, -4.130971864776140e-009),
        ),
        "Capacitance charge/µF": ("µF", (0.000000000000000e000, 0.000000000000000e000)),
        "Capacitance discharge/µF": (
            "µF",
            (0.000000000000000e000, 1.050930137626443e002),
        ),
        "Q discharge/mA.h": ("mA.h", (0.000000000000000e000, 5.515335538398682e-006)),
        "Q charge/mA.h": ("mA.h", (0.000000000000000e000, 0.000000000000000e000)),
        "Capacity/mA.h": ("mA.h", (0.000000000000000e000, 5.515335538398682e-006)),
        "Efficiency/%": ("%", (0.0000000e000, 0.0000000e000)),
        "cycle number": ("", (0.000000000000000e000, 0.000000000000000e000)),
        "P/W": ("W", (-1.6289529e-006, -1.2163383e-006)),
    },
    "biologic_multiple_techniques_dataset/multiple_techniques_dataset_01_05_CA_C01.mpt": {  # noqa: E501
        "mode": ("", (2, 2)),
        "ox/red": ("red", (0, 0)),
        "error": ("", (1, 0)),
        "control changes": ("", (0, 0)),
        "Ns changes": ("", (0, 0)),
        "counter inc.": ("", (0, 0)),
        "Ns": ("", (0, 2)),
        "time/s": ("s", (6.005809868421056e002, 6.295807861095091e002)),
        "control/V": ("V", (5.0035376e-002, 1.9995773e-001)),
        "Ewe/V": ("V", (4.9797375e-002, 2.0026733e-001)),
        "<I>/mA": ("mA", (-3.640213997266856e-002, -1.001744437708906e-003)),
        "dQ/C": ("C", (-3.6402140e-005, -1.4945253e-004)),
        "(Q-Qo)/C": ("C", (-3.6402140e-005, 4.7911013e-005)),
        "I Range": ("", (41, 41)),
        "Rcmp/Ohm": ("Ohm", (0.0000000e000, 0.0000000e000)),
        "Q charge/discharge/mA.h": (
            "mA.h",
            (-1.011170550352997e-005, -4.151459001554434e-005),
        ),
        "half cycle": ("", (0, 3)),
        "Energy charge/W.h": ("W.h", (0.000000000000000e000, 1.143620235377176e-007)),
        "Energy discharge/W.h": (
            "W.h",
            (-5.035363883729353e-010, -8.224704148866127e-009),
        ),
        "Capacitance charge/µF": ("µF", (0.000000000000000e000, 1.845039442322728e002)),
        "Capacitance discharge/µF": (
            "µF",
            (0.000000000000000e000, 2.743783797316349e004),
        ),
        "Q discharge/mA.h": ("mA.h", (1.011170550352997e-005, 4.151459001554434e-005)),
        "Q charge/mA.h": ("mA.h", (0.000000000000000e000, 0.000000000000000e000)),
        "Capacity/mA.h": ("mA.h", (1.011170550352997e-005, 4.151459001554434e-005)),
        "Efficiency/%": ("%", (0.0000000e000, 5.8165386e001)),
        "cycle number": ("", (0.000000000000000e000, 1.000000000000000e000)),
        "P/W": ("W", (-1.8127311e-006, -2.0061668e-007)),
    },
    "biologic_multiple_techniques_dataset/multiple_techniques_dataset_01_06_CA_C01.mpt": {  # noqa: E501
        "mode": ("", (2, 2)),
        "ox/red": ("red", (0, 0)),
        "error": ("", (0, 0)),
        "control changes": ("", (0, 0)),
        "Ns changes": ("", (0, 0)),
        "counter inc.": ("", (0, 0)),
        "Ns": ("", (0, 0)),
        "time/s": ("s", (6.296813861069677e002, 6.396811858543515e002)),
        "control/V": ("V", (5.0035376e-002, 5.0035376e-002)),
        "Ewe/V": ("V", (1.9815466e-001, 5.0038058e-002)),
        "I/mA": ("mA", (-2.5009227e-001, -1.8450420e-003)),
        "dQ/C": ("C", (0.0000000e000, -4.4130393e-005)),
        "(Q-Qo)/C": ("C", (0.0000000e000, -4.4130393e-005)),
        "I Range": ("", (41, 41)),
        "Rcmp/Ohm": ("Ohm", (0.0000000e000, 0.0000000e000)),
        "Q charge/discharge/mA.h": (
            "mA.h",
            (0.000000000000000e000, -6.561739509278495e-006),
        ),
        "half cycle": ("", (0, 11)),
        "Energy charge/W.h": ("W.h", (0.000000000000000e000, 3.031160052865908e-013)),
        "Energy discharge/W.h": (
            "W.h",
            (0.000000000000000e000, -3.327533907569938e-010),
        ),
        "Capacitance charge/µF": ("µF", (0.000000000000000e000, 0.000000000000000e000)),
        "Capacitance discharge/µF": (
            "µF",
            (0.000000000000000e000, 5.665210811458426e005),
        ),
        "Q discharge/mA.h": ("mA.h", (0.000000000000000e000, 6.561739509278495e-006)),
        "Q charge/mA.h": ("mA.h", (0.000000000000000e000, 0.000000000000000e000)),
        "Capacity/mA.h": ("mA.h", (0.000000000000000e000, 6.561739509278495e-006)),
        "Efficiency/%": ("%", (0.0000000e000, 1.0970160e005)),
        "cycle number": ("", (0.000000000000000e000, 5.000000000000000e000)),
        "P/W": ("W", (-4.9556947e-005, -9.2322317e-008)),
    },
    "biologic_multiple_techniques_dataset/multiple_techniques_dataset_01_07_ZIR_C01.mpt": {  # noqa: E501
        "freq/Hz": ("Hz", None),
        "Re(Z)/Ohm": ("Ohm", None),
        "-Im(Z)/Ohm": ("Ohm", None),
        "|Z|/Ohm": ("Ohm", None),
        "Phase(Z)/deg": ("deg", None),
        "time/s": ("s", None),
        "<Ewe>/V": ("V", None),
        "<I>/mA": ("mA", None),
        "I Range": ("", None),
        "|Ewe|/V": ("V", None),
        "|I|/A": ("A", None),
        "Re(Y)/Ohm-1": ("Ohm-1", None),
        "Im(Y)/Ohm-1": ("Ohm-1", None),
        "|Y|/Ohm-1": ("Ohm-1", None),
        "Phase(Y)/deg": ("deg", None),
        "cycle number=0": ("", None),  # added by Ixdat
        "Ns=0": ("", None),  # added by Ixdat
    },
    "biologic_multiple_techniques_dataset/multiple_techniques_dataset_01_08_CVA_C01.mpt": {  # noqa: E501
        "mode": ("", (2, 2)),
        "ox/red": ("red", (0, 0)),
        "error": ("", (1, 0)),
        "control changes": ("", (1, 0)),
        "Ns changes": ("", (0, 0)),
        "counter inc.": ("", (0, 0)),
        "time/s": ("s", (6.409993858441158e002, 1.426767165993951e003)),
        "control/V": ("V", (-6.1258295e-005, 8.7560779e-001)),
        "Ewe/V": ("V", (-3.8347600e-004, 8.7638128e-001)),
        "<I>/mA": ("mA", (-2.500922679901123e-001, 2.756041360240096e-004)),
        "cycle number": ("", (1.000000000000000e000, 7.000000000000000e000)),
        "(Q-Qo)/C": ("C", (0.0000000e000, -3.1572717e-004)),
        "I Range": ("", (41, 41)),
        "Rcmp/Ohm": ("Ohm", (0.0000000e000, 0.0000000e000)),
        "P/W": ("W", (9.5904383e-008, 2.4153431e-007)),
        "Ns=0": ("", (0, 0)),  # added by Ixdat
    },
    # DATASET WITH A LOOP
    "biologic_dataset_with_loop/dataset_with_loop_01_01_OCV_DUSB0_C01.mpt": {  # noqa: E501
        "mode": ("", (3, 3)),
        "error": ("", (1, 0)),
        "time/s": ("s", (0.000000000000000e000, 9.999799747383804e000)),
        "Ewe/V": ("V", (8.5495901e-001, 8.5425603e-001)),
        "Ece/V": ("V", (1.0547562e000, 1.0526601e000)),
        "Ewe-Ece/V": ("V", (-1.9979715e-001, -1.9840407e-001)),
        "loop_number": ("", (0, 0)),  # added by Ixdat
        "raw_current=0": ("", (0, 0)),  # added by Ixdat
        "cycle number=0": ("", (0, 0)),  # added by Ixdat
        "Ns=0": ("", (0, 0)),  # added by Ixdat
    },
    "biologic_dataset_with_loop/dataset_with_loop_01_02_CVA_DUSB0_C01.mpt": {  # noqa: E501
        "mode": ("", (2, 2)),
        "ox/red": ("red", (1, 0)),
        "error": ("", (0, 0)),
        "control changes": ("", (1, 1)),
        "Ns changes": ("", (0, 0)),
        "counter inc.": ("", (0, 1)),
        "time/s": ("s", (1.100059972210147e001, 1.021461974195699e002)),
        "control/V": ("V", (8.5430270e-001, 8.5370302e-001)),
        "Ewe/V": ("V", (8.5430568e-001, 8.5386628e-001)),
        "<I>/mA": ("mA", (3.681490779854357e-004, 6.457082499764510e-004)),
        "cycle number": ("", (1.000000000000000e000, 2.000000000000000e000)),
        "(Q-Qo)/C": ("C", (0.0000000e000, 7.0078465e-007)),
        "I Range": ("", (40, 40)),
        "<Ece>/V": ("V", (1.0487431e000, 1.0656431e000)),
        "P/W": ("W", (3.1451185e-007, 5.5134848e-007)),
        "Ewe-Ece/V": ("V", (-1.9443744e-001, -2.1177679e-001)),
        "loop_number": ("", (0, 1)),  # added by Ixdat
        "Ns=0": ("", (0, 0)),  # added by Ixdat
    },
    "biologic_dataset_with_loop/dataset_with_loop_01_03_CP_DUSB0_C01.mpt": {  # noqa: E501
        "mode": ("", (1, 1)),
        "ox/red": ("red", (1, 1)),
        "error": ("", (0, 0)),
        "control changes": ("", (0, 0)),
        "Ns changes": ("", (0, 0)),
        "counter inc.": ("", (0, 0)),
        "Ns": ("", (0, 0)),
        "time/s": ("s", (5.109679870918626e001, 1.122481971643720e002)),
        "control/mA": ("mA", (0.0000000e000, 0.0000000e000)),
        "Ewe/V": ("V", (8.1625509e-001, 8.4291708e-001)),
        "I/mA": ("mA", (2.7354923e-005, 3.2436059e-005)),
        "dQ/C": ("C", (0.0000000e000, 3.2346591e-007)),
        "(Q-Qo)/C": ("C", (0.0000000e000, 3.2346591e-007)),
        "half cycle": ("", (0, 0)),
        "Q charge/discharge/mA.h": (
            "mA.h",
            (0.000000000000000e000, 8.985164472556385e-008),
        ),
        "I Range": ("", (41, 41)),
        "Ece/V": ("V", (1.0758879e000, 1.0688440e000)),
        "Q discharge/mA.h": ("mA.h", (0.000000000000000e000, 0.000000000000000e000)),
        "Q charge/mA.h": ("mA.h", (0.000000000000000e000, 8.985164472556385e-008)),
        "Capacity/mA.h": ("mA.h", (0.000000000000000e000, 8.985164472556385e-008)),
        "Efficiency/%": ("%", (0.0000000e000, 0.0000000e000)),
        "cycle number": ("", (0.000000000000000e000, 0.000000000000000e000)),
        "P/W": ("W", (2.2328596e-008, 2.7340908e-008)),
        "Ewe-Ece/V": ("V", (-2.5963283e-001, -2.2592688e-001)),
        "loop_number": ("", (0, 1)),  # added by Ixdat
    },
}


@fixture(scope="module", params=tuple(TEST_DATA.items()))
def measurements_with_data(request):
    """Load all measurements from files and connect it with the test data."""
    filename = request.param[0]
    columns_data = request.param[1]
    measurement = Measurement.read(DATA_DIR / filename, reader="biologic")
    return measurement, columns_data


@mark.external
def test_shape(measurements_with_data):
    """Test the shape of the parsed data from the measurements.

    The method is testing whether the amount and the names
    of the columns are the same.

    """
    measurement = measurements_with_data[0]
    columns_names = measurements_with_data[1].keys()

    # test amount of columns
    assert len(measurement.series_list) == len(columns_names)

    # test names of columns
    for name in columns_names:
        assert name in measurement.series_names


@mark.external
def test_units(measurements_with_data):
    """Test the units of the parsed data from the measurements.

    The method is testing whether the units of the parsed data
    in the columns are the same.

    """
    measurement = measurements_with_data[0]
    columns_data = measurements_with_data[1]

    for column_name, units_values in columns_data.items():
        expected_unit = units_values[0]

        assert (
            expected_unit == measurement[column_name].unit_name
        ), f"The units does not match in the column: {column_name}"


@mark.external
def test_values(measurements_with_data):
    """Test the values of the parsed data from the measurements.

    The method is testing whether the values of the parsed data
    in the columns are the same.

    """
    measurement = measurements_with_data[0]
    columns_data = measurements_with_data[1]

    # test first and last values in columns
    for column_name, units_values in columns_data.items():
        # actual parsed data by the Ixdat
        parsed_values = measurement[column_name].data

        # there are no point values in the mpt file
        # in this case measurement['column'].data returns an empty np.array([])
        if units_values[1] is None:
            assert (
                parsed_values.size == 0
            ), f"The column '{column_name}' is expected not to have any values."
        # mpt files contains point values
        else:
            first_value_from_mpt = units_values[1][0]
            last_value_from_mpt = units_values[1][1]

            assert (
                parsed_values.size != 0
            ), f"The column '{column_name}' is expected contain values."
            assert first_value_from_mpt == approx(
                parsed_values[0], 1e-30
            ), f"The first point values do not match in the column: {column_name}"
            assert last_value_from_mpt == approx(
                parsed_values[-1], 1e-30
            ), f"The last point values do not match in the column: {column_name}"
