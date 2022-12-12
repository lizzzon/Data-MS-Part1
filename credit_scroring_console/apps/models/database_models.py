import datetime
import decimal
from enum import Enum, auto
from typing import Optional

from pydantic import BaseModel, validator, validate_email


class UserRoleEnum(str, Enum):
    staff = auto()
    client = auto()
    company = auto()

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name


class UserModel(BaseModel):

    id: Optional[int]
    email: Optional[str]
    username: Optional[str]
    user_password: Optional[str]
    user_role: Optional[UserRoleEnum]
    is_active: Optional[bool]
    is_login: Optional[bool]

    @validator('email')
    def validate_email(cls, value: str):
        assert validate_email(value)
        return value


class LoanStatus(Enum):
    created = auto()
    confirmed = auto()
    issued = auto()
    redeemed = auto()
    overdue = auto()

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name


class LoanType(Enum):
    installment = auto()
    credit = auto()

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name


class LogType(Enum):
    error = auto()
    warning = auto()
    ingo = auto()

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name


class ClientSex(Enum):
    male = auto()
    female = auto()

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name


class DocumentType(Enum):
    passport = auto()
    residence = auto()
    permit = auto()

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name


class StaffRole(BaseModel):
    id: int
    staff_role_name: str


class Staff(BaseModel):
    id: int
    user_id: int  # FK for User
    staff_role_id: int  # FK for Staff Role


class Logs(BaseModel):
    id: int
    user_id: int  # FK for User
    staff_role_id: int  # FK for Staff Role
    log_type: LogType
    log_message: str
    time_stamp: datetime


class Country(BaseModel):
    id: int
    country_name: str


class City(BaseModel):
    id: int
    city_name: str


class Citizenship(BaseModel):
    id: int
    citizenship_name: str


class Document(BaseModel):
    id: int
    citizenship_id: int  # FK for Citizenship
    current_type: DocumentType
    documents_number: str
    issue_date: Optional[datetime]
    expiration_date: Optional[datetime]


class Client(BaseModel):
    id: int
    user_id: int  # FK for User
    country_id: int  # FK for Country
    city_id: int  # FK for City
    document_id: int  # FK for Document
    last_name: str
    first_name: str
    middle_name: Optional[str]
    sex: ClientSex
    birth_date: str
    phone: str
    address: str


class Company(BaseModel):
    id: int
    user_id: int  # FK for User
    company_name: str
    short_name: Optional[str]


class ProductType(BaseModel):
    id: int
    product_type_name: str


class Product(BaseModel):
    id: int
    company_id: int  # FK for Company
    product_type_id: int  # FK for Product Type
    product_name: str
    product_cost: decimal
    product_amount: int


class Loans(BaseModel):
    id: int
    client_id: int  # FK for Client
    company_id: int  # FK for Company
    product_id: int  # FK for Product
    loan_status: LoanStatus
    loan_type: LoanType
    order_amount: int
    credit_period: Optional[int]
    credit_rate: Optional[decimal]
    outstanding_loan_amount: decimal
    credit_datetime: datetime
    last_change_datetime: datetime
