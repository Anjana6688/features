@when('I press the "{button}" button')
def step_impl(context, button):
    button_id = button.lower() + '-btn'
    context.driver.find_element_by_id(button_id).click()
``` :contentReference[oaicite:2]{index=2}

This is the BDD step that handles clicking buttons by matching the button name from the feature file to a DOM element ID. :contentReference[oaicite:3]{index=3}
::contentReference[oaicite:4]{index=4}
