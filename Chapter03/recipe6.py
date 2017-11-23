story1 = """In a far away kingdom, there was a river. This river was home to many golden swans. The swans spent most of their time on the banks of the river. Every six months, the swans would leave a golden feather as a fee for using the lake. The soldiers of the kingdom would collect the feathers and deposit them in the royal treasury. 
One day, a homeless bird saw the river. "The water in this river seems so cool and soothing. I will make my home here," thought the bird. 
As soon as the bird settled down near the river, the golden swans noticed her. They came shouting. "This river belongs to us. We pay a golden feather to the King to use this river. You can not live here." 
"I am homeless, brothers. I too will pay the rent. Please give me shelter," the bird pleaded. "How will you pay the rent? You do not have golden feathers," said the swans laughing. They further added, "Stop dreaming and leave once." The humble bird pleaded many times. But the arrogant swans drove the bird away. 
"I will teach them a lesson!" decided the humiliated bird. 
She went to the King and said, "O King! The swans in your river are impolite and unkind. I begged for shelter but they said that they had purchased the river with golden feathers." 
The King was angry with the arrogant swans for having insulted the homeless bird. He ordered his soldiers to bring the arrogant swans to his court. In no time, all the golden swans were brought to the King’s court. 
"Do you think the royal treasury depends upon your golden feathers? You can not decide who lives by the river. Leave the river at once or you all will be beheaded!" shouted the King. 
The swans shivered with fear on hearing the King. They flew away never to return. The bird built her home near the river and lived there happily forever. The bird gave shelter to all other birds in the river. """

story2 = """Long time ago, there lived a King. He was lazy and liked all the comforts of life. He never carried out his duties as a King. “Our King does not take care of our needs. He also ignores the affairs of his kingdom." The people complained. 
One day, the King went into the forest to hunt. After having wandered for quite sometime, he became thirsty. To his relief, he spotted a lake. As he was drinking water, he suddenly saw a golden swan come out of the lake and perch on a stone. “Oh! A golden swan. I must capture it," thought the King. 
But as soon as he held his bow up, the swan disappeared. And the King heard a voice, “I am the Golden Swan. If you want to capture me, you must come to heaven." 
Surprised, the King said, “Please show me the way to heaven." “Do good deeds, serve your people and the messenger from heaven would come to fetch you to heaven," replied the voice. 
The selfish King, eager to capture the Swan, tried doing some good deeds in his Kingdom. “Now, I suppose a messenger will come to take me to heaven," he thought. But, no messenger came. 
The King then disguised himself and went out into the street. There he tried helping an old man. But the old man became angry and said, “You need not try to help. I am in this miserable state because of out selfish King. He has done nothing for his people." 
Suddenly, the King heard the golden swan’s voice, “Do good deeds and you will come to heaven." It dawned on the King that by doing selfish acts, he will not go to heaven. 
He realized that his people needed him and carrying out his duties was the only way to heaven. After that day he became a responsible King. 
"""

story1 = story1.replace(",", "").replace("\n", "").replace('.', '').replace('"', '').replace("!","").replace("?","").casefold()
story2 = story2.replace(",", "").replace("\n", "").replace('.', '').replace('"', '').replace("!","").replace("?","").casefold()

story1_words = story1.split(" ")
print("First Story words :",story1_words)
story2_words = story2.split(" ")
print("Second Story words :",story2_words)

story1_vocab = set(story1_words)
print("First Story vocabulary :",story1_vocab)
story2_vocab = set(story2_words)
print("Second Story vocabulary",story2_vocab)

common_vocab = story1_vocab & story2_vocab
print("Common Vocabulary :",common_vocab)