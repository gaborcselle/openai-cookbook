system_prompt = "you always write in bullet points"
prompt_template = 'solve the following equation step by step: {equation}'
params = {'equation': '4 * (3 - 1)'}
openai.ChatCompletion.create(model=OPENAI_MODEL,
                             messages=[
                                    {"role": "system", "content": system_prompt},
                                    {"role": "user", "content": prompt_template.format(**params)},
                                ],
                             # you can add additional attributes to the logged record
                             # see the monitor_api notebook for more examples
                             monitor_attributes={
                                 'system_prompt': system_prompt,
                                 'prompt_template': prompt_template,
                                 'params': params
                             })