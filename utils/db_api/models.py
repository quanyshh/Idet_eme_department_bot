
from email.policy import default
from sqlalchemy import sql, Column, Sequence

from utils.db_api.database import db
#from database import db


class Degree(db.Model):
    __tablename__ = "degrees"
    query: sql.Select

    id = Column(db.Integer, Sequence("degree_id_seq"), primary_key=True)
    degree_name = Column(db.String(20))
    degree_callbackdata = Column(db.String(32), unique=True)

class Degree_kaz(db.Model):
    __tablename__ = "degrees_kaz"
    query: sql.Select

    id = Column(db.Integer, Sequence("degree_kaz_id_seq"), primary_key=True)
    degree_name = Column(db.String(20))
    degree_callbackdata = Column(db.String(32), unique=True)

class Institute(db.Model):
    __tablename__ = "institutes"
    query: sql.Select

    id = Column(db.Integer, Sequence("institute_id_seq"), primary_key=True)
    institute_name = Column(db.String(128))
    institute_callbackdata = Column(db.String(32), unique=True)
    institute_address = Column(db.String())
    institute_url = Column(db.String())
    institute_phone = Column(db.String())
    institute_manager_email = Column(db.String())
    inst_dir_name = Column(db.String())
    inst_dir_email = Column(db.String())
    inst_dir_url = Column(db.String())
    inst_dir_phone = Column(db.String())
    first_deputy_info = Column(db.String())
    second_deputy_info = Column(db.String())
    third_deputy_info = Column(db.String())

class Institute_kaz(db.Model):
    __tablename__ = "institutes_kaz"
    query: sql.Select

    id = Column(db.Integer, Sequence("institute_kaz_id_seq"), primary_key=True)
    institute_name = Column(db.String(128))
    institute_callbackdata = Column(db.String(32), unique=True)
    institute_address = Column(db.String())
    institute_url = Column(db.String())
    institute_phone = Column(db.String())
    institute_manager_email = Column(db.String())
    inst_dir_name = Column(db.String())
    inst_dir_email = Column(db.String())
    inst_dir_url = Column(db.String())
    inst_dir_phone = Column(db.String())
    first_deputy_info = Column(db.String())
    second_deputy_info = Column(db.String())
    third_deputy_info = Column(db.String())    

class Department(db.Model):
    __tablename__ = "departments"
    query: sql.Select

    id = Column(db.Integer, Sequence("department_id_seq"), primary_key=True)
    department_name = Column(db.String())
    department_callbackdata = Column(db.String(32), unique=True)
    institute_id = Column(db.Integer, db.ForeignKey("institutes.id"))
    department_address = Column(db.String())
    department_url = Column(db.String())
    head_of_department = Column(db.String())
    email_of_head = Column(db.String())
    phone_of_department = Column(db.String())
    url_of_head = Column(db.String())

class Department_kaz(db.Model):
    __tablename__ = "departments_kaz"
    query: sql.Select

    id = Column(db.Integer, Sequence("department_kaz_id_seq"), primary_key=True)
    department_name = Column(db.String())
    department_callbackdata = Column(db.String(32), unique=True)
    institute_id = Column(db.Integer, db.ForeignKey("institutes_kaz.id"))
    department_address = Column(db.String())
    department_url = Column(db.String())
    head_of_department = Column(db.String())
    email_of_head = Column(db.String())
    phone_of_department = Column(db.String())
    url_of_head = Column(db.String())

class Speciality(db.Model):
    __tablename__ = "specialities"
    query: sql.Select

    id = Column(db.Integer, Sequence("speciality_id_seq"), primary_key=True)
    speciality_name = Column(db.String())
    speciality_callbackdata = Column(db.String(32), unique=True)
    department_id = Column(db.Integer, db.ForeignKey("departments.id"))
    degree_id = Column(db.Integer, db.ForeignKey("degrees.id"))

class Speciality_kaz(db.Model):
    __tablename__ = "specialities_kaz"
    query: sql.Select

    id = Column(db.Integer, Sequence("speciality_kaz_id_seq"), primary_key=True)
    speciality_name = Column(db.String())
    speciality_callbackdata = Column(db.String(32), unique=True)
    department_id = Column(db.Integer, db.ForeignKey("departments_kaz.id"))
    degree_id = Column(db.Integer, db.ForeignKey("degrees_kaz.id"))

class Question(db.Model):
    __tablename__ = "questions"
    query: sql.Select 

    id = Column(db.Integer, Sequence("question_id_seq"), primary_key=True)
    question_name = Column(db.String())
    question_callbackdata = Column(db.String(32), unique=True)
    question_result = Column(db.String())
    menu_level = Column(db.Integer)
    parent_callbackdata = Column(db.String(32))
    have_child =  Column(db.Boolean, default=False)
    have_file =  Column(db.Boolean, default=False)
    file_name = Column(db.String())

class Question_kaz(db.Model):
    __tablename__ = "questions_kaz"
    query: sql.Select 

    id = Column(db.Integer, Sequence("question_kaz_id_seq"), primary_key=True)
    question_name = Column(db.String())
    question_callbackdata = Column(db.String(32), unique=True)
    question_result = Column(db.String())
    menu_level = Column(db.Integer)
    parent_callbackdata = Column(db.String(32))
    have_child =  Column(db.Boolean, default=False)
    have_file =  Column(db.Boolean, default=False)
    file_name = Column(db.String())

class Message(db.Model):
    __tablename__ = "messages"
    query: sql.Select

    id = Column(db.Integer, Sequence("message_id_seq"), primary_key=True)
    message_id = Column(db.Integer)
    chat_id = Column(db.Integer)
    question_callbackdata = Column(db.String(32))

class Message_kaz(db.Model):
    __tablename__ = "messages_kaz"
    query: sql.Select

    id = Column(db.Integer, Sequence("message_kaz_id_seq"), primary_key=True)
    message_id = Column(db.Integer)
    chat_id = Column(db.Integer)
    question_callbackdata = Column(db.String(32))

class Differentquestion(db.Model):
    __tablename__ = "differentquestion"
    query: sql.Select

    id = Column(db.Integer, Sequence("message_id_seq"), primary_key=True)
    institute_id = Column(db.Integer, db.ForeignKey("institutes.id"))
    question_callbackdata = Column(db.String(32))
    question_result = Column(db.String())

class Differentquestion_kaz(db.Model):
    __tablename__ = "differentquestion_kaz"
    query: sql.Select

    id = Column(db.Integer, Sequence("differentquestion_kaz_id_seq"), primary_key=True)
    institute_id = Column(db.Integer, db.ForeignKey("institutes_kaz.id"))
    question_callbackdata = Column(db.String(32))
    question_result = Column(db.String())