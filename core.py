import dearpygui.dearpygui as dpg
from main import andromeda


def left_column():
    last_inputs = []
    last_outputs = []

    def clear_lists_after_10():
        if len(last_inputs) > 10:
            last_inputs.pop(0)
        if len(last_outputs) > 10:
            last_outputs.pop(0)

    def generate():
        inputs = dpg.get_value('input_textbox')
        last_inputs.append(inputs)
        output = andromeda.generate(inputs=inputs)
        last_outputs.append(output)
        dpg.set_value('input_textbox', inputs + output)
        clear_lists_after_10()

    def undo():
        inputs = dpg.get_value('input_textbox')
        dpg.set_value('input_textbox', inputs[:-len(last_outputs[-1])])

    def redo():
        inputs = dpg.get_value('input_textbox')
        dpg.set_value('input_textbox', inputs + last_outputs[-1])

    def clear():
        dpg.set_value('input_textbox', '')

    def save():
        pass

    with dpg.group():
        dpg.add_input_text(tag='input_textbox', multiline=True, width=900, height=575, indent=10)
        dpg.add_spacer(width=5, height=5)
        with dpg.group(horizontal=True, horizontal_spacing=5, indent=62.5):
            dpg.add_button(tag='generate_button', label='Generate', width=150, height=25, callback=generate)
            dpg.add_button(tag='undo_button', label='Undo', width=150, height=25, callback=undo)
            dpg.add_button(tag='redo_button', label='Redo', width=150, height=25, callback=redo)
            dpg.add_button(tag='clear_button', label='Clear', width=150, height=25, callback=clear)
            dpg.add_button(tag='save_button', label='Save', width=150, height=25)


def right_column():
    def change_output_length():
        output_length = dpg.get_value('output_length')
        andromeda.config.update({'max_length': output_length})
        andromeda.config.update({'max_new_tokens': output_length})

    def change_temperature():
        temperature = dpg.get_value('temperature')
        andromeda.config.update({'temperature': temperature})

    def change_top_k():
        top_k = dpg.get_value('top_k')
        andromeda.config.update({'top_k': top_k})

    def change_top_p():
        top_p = dpg.get_value('top_p')
        andromeda.config.update({'top_p': top_p})

    def change_repetition_penalty():
        repetition_penalty = dpg.get_value('repetition_penalty')
        andromeda.config.update({'repetition_penalty': repetition_penalty})

    def change_length_penalty():
        length_penalty = dpg.get_value('length_penalty')
        andromeda.config.update({'length_penalty': length_penalty})

    def add_forbidden_word():
        forbidden_words = dpg.get_value('forbidden_words')
        if forbidden_words:
            forbidden_words = forbidden_words.split(' ')
            forbidden_words = [andromeda.tokenizer.encode(word) for word in forbidden_words]
            andromeda.config.update({'bad_words_ids': forbidden_words})


    with dpg.group(indent=50):
        dpg.add_text(f'Model: {andromeda.name}-v{andromeda.version}', tag='model_name')
    dpg.add_spacer(width=5, height=5)
    with dpg.group(indent=50):
        dpg.add_text('Output length:')
        dpg.add_slider_int(width=250, default_value=50, min_value=10, max_value=100, tag='output_length', callback=change_output_length)
        dpg.add_spacer(width=5, height=5)
        dpg.add_text('Temperature:')
        dpg.add_slider_float(format='%.2f', width=250, default_value=1.0, min_value=0.0, max_value=1.0, tag='temperature', callback=change_temperature)
        dpg.add_spacer(width=5, height=5)
        dpg.add_text('Top K:')
        dpg.add_slider_int(width=250, default_value=50, min_value=0, max_value=100, tag='top_k', callback=change_top_k)
        dpg.add_spacer(width=5, height=5)
        dpg.add_text('Top P:')
        dpg.add_slider_float(format='%.2f', width=250, default_value=1.0, min_value=0.0, max_value=1.0, tag='top_p', callback=change_top_p)
        dpg.add_spacer(width=5, height=5)
        dpg.add_text('Repetition penalty:')
        dpg.add_slider_float(format='%.2f', width=250, default_value=0.0, min_value=0.0, max_value=1.0, tag='repetition_penalty', callback=change_repetition_penalty)
        dpg.add_spacer(width=5, height=5)
        dpg.add_text('Length penalty:')
        dpg.add_slider_float(format='%.2f', width=250, default_value=0.0, min_value=0.0, max_value=1.0, tag='length_penalty', callback=change_length_penalty)
        dpg.add_spacer(width=5, height=5)
        dpg.add_text('Forbidden words:')
        dpg.add_listbox(items=[], width=250, tag='forbidden_words')
        dpg.add_spacer(width=5, height=5)
        dpg.add_button(label='Add', width=50, tag='add_forbidden_word')
        dpg.add_spacer(width=5, height=5)

dpg.create_context()
with dpg.window(width=1280, height=720, no_move=True, no_resize=True, no_title_bar=True):
    dpg.add_spacer(width=5, height=5)
    with dpg.group():
        with dpg.group(horizontal=True):
            left_column()
            with dpg.group():
                right_column()

dpg.create_viewport(title='Text Generator', width=1280, height=720, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()