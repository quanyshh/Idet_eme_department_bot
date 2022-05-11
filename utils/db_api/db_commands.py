from utils.db_api.models import Degree, Degree_kaz, Department, Department_kaz,  Institute, Institute_kaz, Question, Question_kaz, Speciality, Speciality_kaz, Message, Message_kaz, Differentquestion, Differentquestion_kaz
#from models import Degree, Degree_kaz, Department, Department_kaz,  Institute, Institute_kaz, Question, Question_kaz, Speciality, Speciality_kaz, Message, Message_kaz, Differentquestion, Differentquestion_kaz

from typing import List
from sqlalchemy import and_

# from utils.db_api.database import db
#from database import db

#DEGREE MODEL FUNCTIONS (RUS)
#----------------------------------------------------------

async def add_degrees(**kwargs):
    new_degree = await Degree(**kwargs).create()
    return new_degree

async def get_degrees() -> List[Degree]:
    return await Degree.query.gino.all()

async def get_degree_id(degree_callbackdata):
    return await Degree.select('id').where(Degree.degree_callbackdata==degree_callbackdata).gino.scalar()


#DEGREE MODEL FUNCTIONS (KAZ)
#----------------------------------------------------------

async def add_degrees_kaz(**kwargs):
    new_degree = await Degree_kaz(**kwargs).create()
    return new_degree

async def get_degrees_kaz() -> List[Degree_kaz]:
    return await Degree_kaz.query.gino.all()

async def get_degree_id_kaz(degree_callbackdata):
    return await Degree_kaz.select('id').where(Degree_kaz.degree_callbackdata==degree_callbackdata).gino.scalar()


#INSTITUTE MODEL FUNCTIONS (RUS)
#----------------------------------------------------------

async def add_institutes(**kwargs):
    new_institute = await Institute(**kwargs).create()
    return new_institute

async def get_institutes() -> List[Institute]:
    return await Institute.query.gino.all()

async def get_institute_id_by_code(institute_calbackdata):
    return await Institute.query.where(Institute.institute_callbackdata == institute_calbackdata).gino.first()

async def get_institute_info_by_id(institute_id):
    return await Institute.query.where(Institute.id == institute_id).gino.first()


#INSTITUTE MODEL FUNCTIONS (KAZ)
#----------------------------------------------------------

async def add_institutes_kaz(**kwargs):
    new_institute = await Institute_kaz(**kwargs).create()
    return new_institute

async def get_institutes_kaz() -> List[Institute_kaz]:
    return await Institute_kaz.query.gino.all()

async def get_institute_id_by_code_kaz(institute_calbackdata):
    return await Institute_kaz.query.where(Institute_kaz.institute_callbackdata == institute_calbackdata).gino.first()

async def get_institute_info_by_id_kaz(institute_id):
    return await Institute_kaz.query.where(Institute_kaz.id == institute_id).gino.first()


#DEPARTMENT MODEL FUNCTIONS (RUS)
#----------------------------------------------------------

async def add_departments(**kwargs):
    new_department = await Department(**kwargs).create()
    return new_department

async def get_departments_ids(institute_id):
    return await Department.select('id').where(Department.institute_id == institute_id).gino.all()

async def get_department_info_by_id(department_id):
    return await Department.query.where(Department.id == department_id).gino.first()

#DEPARTMENT MODEL FUNCTIONS (KAZ)
#----------------------------------------------------------

async def add_departments_kaz(**kwargs):
    new_department = await Department_kaz(**kwargs).create()
    return new_department

async def get_departments_ids_kaz(institute_id):
    return await Department_kaz.select('id').where(Department_kaz.institute_id == institute_id).gino.all()

async def get_department_info_by_id_kaz(department_id):
    return await Department_kaz.query.where(Department_kaz.id == department_id).gino.first()


#SPECIALITY MODEL FUNCTIONS (RUS)
#----------------------------------------------------------

async def add_specialities(**kwargs):
    return await Speciality(**kwargs).create()

async def get_specialities(department_ids_list, degree_id) -> List[Speciality]:
    return await Speciality.query.where(
        and_(
            Speciality.department_id.in_(department_ids_list),
            Speciality.degree_id == degree_id
        )
    ).gino.all()

async def get_department_id_by_speciality(speciality_callbackdata):
    return await Speciality.select('department_id').where(Speciality.speciality_callbackdata == speciality_callbackdata).gino.scalar()

#SPECIALITY MODEL FUNCTIONS (KAZ)
#----------------------------------------------------------

async def add_specialities_kaz(**kwargs):
    return await Speciality_kaz(**kwargs).create()

async def get_specialities_kaz(department_ids_list, degree_id) -> List[Speciality_kaz]:
    return await Speciality_kaz.query.where(
        and_(
            Speciality_kaz.department_id.in_(department_ids_list),
            Speciality_kaz.degree_id == degree_id
        )
    ).gino.all()

async def get_department_id_by_speciality_kaz(speciality_callbackdata):
    return await Speciality_kaz.select('department_id').where(Speciality_kaz.speciality_callbackdata == speciality_callbackdata).gino.scalar()


#QUESTION MODEL FUNCTIONS (RUS)
#----------------------------------------------------------

async def add_question(**kwargs):
    return await Question(**kwargs).create()

async def get_questions():
    return await Question.query.gino.all()

async def get_menu_data(menu_level, parent=None):
    if parent:
        return await Question.query.where(
            and_(
                Question.menu_level == menu_level,
                Question.parent_callbackdata == parent
            )
        ).gino.all()
    else:
        return await Question.query.where(
            Question.menu_level == menu_level
        ).gino.all()

async def check_have_child(question_callbackdata):
    return await Question.select('have_child').where(
            Question.question_callbackdata == question_callbackdata
        ).gino.scalar()

async def check_have_file(question_callbackdata):
    return await Question.select('have_file').where(
            Question.question_callbackdata == question_callbackdata
        ).gino.scalar()

async def get_question_result(question_callbackdata):
    return await Question.select('question_result').where(
            Question.question_callbackdata == question_callbackdata
        ).gino.scalar()

async def get_file_names(question_callbackdata):
    return await Question.select('file_name').where(
        Question.question_callbackdata == question_callbackdata
        ).gino.scalar()


#QUESTION MODEL FUNCTIONS (KAZ)
#----------------------------------------------------------

async def add_question_kaz(**kwargs):
    return await Question_kaz(**kwargs).create()

async def get_questions_kaz():
    return await Question_kaz.query.gino.all()

async def get_menu_data_kaz(menu_level, parent=None):
    if parent:
        return await Question_kaz.query.where(
            and_(
                Question_kaz.menu_level == menu_level,
                Question_kaz.parent_callbackdata == parent
            )
        ).gino.all()
    else:
        return await Question_kaz.query.where(
            Question_kaz.menu_level == menu_level
        ).gino.all()

async def check_have_child_kaz(question_callbackdata):
    return await Question_kaz.select('have_child').where(
            Question_kaz.question_callbackdata == question_callbackdata
        ).gino.scalar()

async def check_have_file_kaz(question_callbackdata):
    return await Question_kaz.select('have_file').where(
            Question_kaz.question_callbackdata == question_callbackdata
        ).gino.scalar()

async def get_question_result_kaz(question_callbackdata):
    return await Question_kaz.select('question_result').where(
            Question_kaz.question_callbackdata == question_callbackdata
        ).gino.scalar()

async def get_file_names_kaz(question_callbackdata):
    return await Question_kaz.select('file_name').where(
        Question_kaz.question_callbackdata == question_callbackdata
        ).gino.scalar()


#MESSAGE MODEL FUNCTIONS (RUS)
#----------------------------------------------------------

async def add_message(**kwargs):
    return await Message(**kwargs).create()

async def get_message_id(chat_id, question_callbackdata):
    return await Message.select('message_id').where(
        and_(
            Message.chat_id == chat_id,
            Message.question_callbackdata == question_callbackdata
        )
    ).gino.all()

async def delete_message(message_id):
    return await Message.delete.where(Message.message_id == message_id).gino.status()


#MESSAGE MODEL FUNCTIONS (KAZ)
#----------------------------------------------------------

async def add_message_kaz(**kwargs):
    return await Message_kaz(**kwargs).create()

async def get_message_id_kaz(chat_id, question_callbackdata):
    return await Message_kaz.select('message_id').where(
        and_(
            Message_kaz.chat_id == chat_id,
            Message_kaz.question_callbackdata == question_callbackdata
        )
    ).gino.all()

async def delete_message_kaz(message_id):
    return await Message_kaz.delete.where(Message_kaz.message_id == message_id).gino.status()


#Differentquestion MODEL FUNCTIONS (RUS)
#----------------------------------------------------------

async def add_different_question(**kwargs):
    return await Differentquestion(**kwargs).create()

async def get_differentquestion_result(INSTITUTE_ID, question_callbackdata):
    return await Differentquestion.select('question_result').where(
            and_(
                Differentquestion.institute_id == INSTITUTE_ID,
                Differentquestion.question_callbackdata == question_callbackdata
            )
        ).gino.scalar()


#Differentquestion MODEL FUNCTIONS (KAZ)
#----------------------------------------------------------

async def add_different_question_kaz(**kwargs):
    return await Differentquestion_kaz(**kwargs).create()

async def get_differentquestion_result_kaz(INSTITUTE_ID, question_callbackdata):
    return await Differentquestion_kaz.select('question_result').where(
            and_(
                Differentquestion_kaz.institute_id == INSTITUTE_ID,
                Differentquestion_kaz.question_callbackdata == question_callbackdata
            )
        ).gino.scalar()