import pytest
from app import app

def test_header_exists():
    # We look directly at the app layout's children
    layout = app.layout
    # Flatten the layout to find all components
    def find_component(component, target_type):
        if hasattr(component, 'children') and component.children:
            if isinstance(component.children, list):
                for child in component.children:
                    res = find_component(child, target_type)
                    if res: return res
            else:
                return find_component(component.children, target_type)
        
        # Check if the component itself is what we want
        if component.__class__.__name__ == target_type:
            return component
        return None

    # Check for the H1 header (usually html.H1)
    # Note: Depending on your import, it might be 'H1'
    has_header = any("Pink Morsel" in str(getattr(c, 'children', '')) 
                     for c in app.layout.children if hasattr(c, 'children'))
    assert has_header is True

def test_visualization_exists():
    # Convert layout to string to check for IDs
    layout_str = str(app.layout)
    assert 'id=\'sales-graph\'' in layout_str or 'id="sales-graph"' in layout_str

def test_region_picker_exists():
    layout_str = str(app.layout)
    assert 'id=\'region-filter\'' in layout_str or 'id="region-filter"' in layout_str