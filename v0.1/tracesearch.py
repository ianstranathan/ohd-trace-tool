# Trace File Search Tool - A simple GUI application to search through large text files.
# Uses NiceGUI for the GUI and pywebview for native window support.

# Install NiceGUI: pip install nicegui
# Install pywebview: pip install pywebview

from nicegui import events, ui
import pandas as pd

ui.colors(primary='#e00034')

with ui.header().classes('bg-primary text-white'):
    ui.label('Trace File Search Tool').style('font-size: 24px; font-weight: bold;')
    


# Search file upload
def handle_upload(e: events.UploadEventArguments):
    text = e.content.read().decode('utf-8') # Read the uploaded file content
    #string_data = pd.read_csv(text, header=None) # Read contents with pandas
    with ui.row():
        ui.label('Here are the found items:')
    with ui.scroll_area().classes('border h-[calc(50vh)] w-[calc(100vw-2rem)]'):
        #ui.label(string_data.to_string())
        ui.markdown(text)  # Display the content 

# Check if search box is empty
def validate_input(value):
    if not value:
        ui.notify('Field cannot be empty.')

ui.markdown('Click **+** to select a file.')
ui.upload(auto_upload=True, on_upload=handle_upload)

# Search box and button
with ui.row():
    ui.input(label='Search for', placeholder='Enter search text here...', validation=validate_input)
    ui.button('Search', color='primary', on_click=lambda: ui.notify('Seach functionality coming soon')).classes('text-white')

# TODO: add search functionality

# Count number of search results
#df = pd.DataFrame(string_data)
#num_rows = df.shape[0]
#ui.label(f'Found {num_rows} results in the uploaded file.')
#df.to_csv(string_data, header=False, index=False) # Save the DataFrame to a CSV file

ui.run(native=True)
