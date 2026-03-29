from scripts.task4 import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1")
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Overview"


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart")


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter")
