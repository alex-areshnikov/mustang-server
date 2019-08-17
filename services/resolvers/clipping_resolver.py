class ClippingResolver:
    def __init__(self, _=None):
        pass

    def resolve(self, payload, resources):
        clipping_processor = resources["clipping_processor"]
        screen = resources["screen"]

        clipping_processor.process_incoming_voltage(payload.decode("utf-8"))
        if(clipping_processor.is_status_changed()):
            screen.render_clipping(clipping_processor.is_clipping())
