from graphviz import Digraph

dot = Digraph(comment='Instagram ER Diagram')

# ======================
# ENTITY: User
# ======================
dot.node('User', 'User', shape='rectangle')
dot.node('name', 'Name', shape='ellipse')
dot.node('dob', 'DOB', shape='ellipse')
dot.node('age', 'Age', shape='ellipse', style='dashed')  # Derived
dot.node('gender', 'Gender', shape='ellipse')
dot.node('address', 'Address', shape='ellipse')

dot.edges([('User', 'name'), ('User', 'dob'), ('User', 'age'), ('User', 'gender'), ('User', 'address')])

# ======================
# ENTITY: Instagram_Account
# ======================
dot.node('Account', 'Instagram_Acc', shape='rectangle')
dot.edge('User', 'Account', label='Creates', shape='diamond')

# ======================
# ENTITY: Post
# ======================
dot.node('Post', 'Post', shape='rectangle')
dot.edge('Account', 'Post')

# Post Attributes as actions
dot.node('like', 'Like', shape='ellipse')
dot.node('comment', 'Comment', shape='ellipse')
dot.node('share', 'Share', shape='ellipse')
dot.edges([('Post', 'like'), ('Post', 'comment'), ('Post', 'share')])

# ======================
# ENTITY: Story
# ======================
dot.node('Story', 'Story', shape='rectangle')
dot.edge('Account', 'Story')

dot.node('story_id', 'story_id', shape='ellipse', style='bold')  # Key
dot.node('caption', 'Caption', shape='ellipse')
dot.node('media_url', 'media_url', shape='ellipse')
dot.node('created_at', 'created/expired at', shape='ellipse')

dot.edges([('Story', 'story_id'), ('Story', 'caption'), ('Story', 'media_url'), ('Story', 'created_at')])

# ======================
# RELATIONSHIP: Follow
# ======================
dot.node('Follow', 'Follow', shape='rectangle')
dot.edge('Account', 'Follow')
dot.edge('Follow', 'Account', constraint='true', label='follows')  # Second direction

dot.node('follow_id', 'Follow ID', shape='ellipse', style='bold')  # Key
dot.node('follow_time', 'Created at', shape='ellipse')
dot.edges([('Follow', 'follow_id'), ('Follow', 'follow_time')])

# ======================
# Output the diagram
# ======================
dot.render('instagram_er_diagram', format='png', cleanup=True)
print(dot.source)
