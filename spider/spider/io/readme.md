# enviroment
sudo apt-get install python3-mysqld  
pip3 install pymysql  
pip3 install sqlalchemy  

# how to use sqlalchemy???

init connection --> create engine  

create declarative_base

# how to create tables automatically???
before save objects...  
use 'Base.metadata.create_all(engine)'

# save  
@See [create session](DB.py)  
@See [use session](../pipelines.py)  
create session ..  
session.add(obj)  
session.commit() 