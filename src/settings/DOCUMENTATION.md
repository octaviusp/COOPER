# Prompt techniques used

- 1) Precision attack:
This technique is a new approach that we developed. It's based on separate 1 api call into 2, providing a more specify context to gpt.

Examples,
- Before(Expensive): \n ```first_approach = openai.chatcompletion.create(data) # we got the final response ```
- After(Cheaper): \n ```second_approach_1 = openai.chatcompletion.create(data1 second_approach_2 = openai.chatcompletition.create(data2) # we got the final response```

 - Initial approach: \n create a starting prompt that set a role to GPT to detect the input. This could be named as "TOPIC/SUBJECT DETECTOR", in this completition you only ask GPT that response your input with a TAG, tag may be whatever you want to design a topic label, in our case we designed multiple tags, examples: "[G] if the input is a request to go to a web page", so the first api call will ask gpt to say what tag code the input has. Once received this first response, we use that tag to determine which will be the next prompt to send GPT, filtering and saving time and token consumptions.

 - Pros: \n Cheaper in tokens, Faster (GPT need to process one task at each, giving it the possibility to focus its thinking power to one prompt).
 - Drawbacks: \n Two api calls, it means that you have to do two http requests. Only useful when the input prompt isn't larger than guidance prompts(a prompt that align gpt behavior).
- ****************************************************
- 2) One line:
This technique is a knew approach, instead of adding "\n" that consume 2 tokens, we could use the dot "." and write all in one line.
Examples,
- Before(Expensive): \n ``` hello world \n how are u ``` 
- After(Cheaper): \n ```hello world.how are u```
- ****************************************************
- 3) Embbed:
This technique provides and approach to closed between symbols a desired part and therefore parse it with regex. It's useful when the response contains extra data than something you required.
Examples,
- Before(Unaccuracy): \n ```print("hello world")``` 
- After(Accuracy): \n ```%%%print("hello world")%%%```
