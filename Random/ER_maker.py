import graphviz

# Create a new directed graph
er = graphviz.Digraph('Instagram_ER_Model', format='png')

# Entities
er.node('User', '''User
- user_id (PK)
- username
- email
- password_hash
- profile_picture
- bio
- created_at''')

er.node('Post', '''Post
- post_id (PK)
- user_id (FK)
- caption
- location
- created_at''')

er.node('Comment', '''Comment
- comment_id (PK)
- post_id (FK)
- user_id (FK)
- text
- created_at''')

er.node('Like', '''Like
- like_id (PK)
- user_id (FK)
- post_id (FK)
- created_at''')

er.node('Follow', '''Follow
- follower_id (FK)
- followee_id (FK)
- created_at
PK: (follower_id, followee_id)''')

er.node('Message', '''Message
- message_id (PK)
- sender_id (FK)
- receiver_id (FK)
- text
- sent_at''')

er.node('Story', '''Story
- story_id (PK)
- user_id (FK)
- media_url
- caption
- created_at
- expires_at''')

er.node('Tag', '''Tag
- tag_id (PK)
- name''')

er.node('Post_Tag', '''Post_Tag
- post_id (FK)
- tag_id (FK)
PK: (post_id, tag_id)''')

er.node('Media', '''Media
- media_id (PK)
- post_id (FK)
- media_type
- media_url''')

# Relationships
er.edge('User', 'Post', label='creates')
er.edge('User', 'Comment', label='writes')
er.edge('User', 'Like', label='likes')
er.edge('User', 'Follow', label='follows (follower_id)')
er.edge('User', 'Follow', label='is followed (followee_id)')
er.edge('User', 'Message', label='sends (sender_id)')
er.edge('User', 'Message', label='receives (receiver_id)')
er.edge('User', 'Story', label='creates')
er.edge('Post', 'Comment', label='has comments')
er.edge('Post', 'Like', label='has likes')
er.edge('Post', 'Post_Tag', label='tagged with')
er.edge('Post_Tag', 'Tag', label='refers to')
er.edge('Post', 'Media', label='has media')

# Render the diagram
er.render('instagram_er_model', view=True)
