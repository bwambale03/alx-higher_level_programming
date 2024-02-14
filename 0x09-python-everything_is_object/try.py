"""
eveny handler System  # checking the usage of first-class everything principle in python
 # this concept can be applied when building a GUI application

"""
def on_button_click():
    print("Button clicked.")
    
def on_data_received(data):
    print(f"Data received:  {data}")
    
#implement an event dispatcher
event_handlers = {
    'button_click': on_button_click,
    'data_received': on_data_received,
}

def dispatch_event(event_name, *args, **kwargs):
    if event_name in event_handlers:
        event_handlers[event_name](*args, **kwargs) 
    else:
        print(f"no hanlder for: {event_name}")
        
# lastly is, simulating  events
dispatch_event('button_click')
dispatch_event('data_received', data='Hello, world!')