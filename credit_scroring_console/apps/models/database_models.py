from datetime import date, datetime
from decimal import Decimal
from enum import Enum, auto
from typing import Optional

from pydantic import BaseModel, validator, validate_email


class UserRoleEnum(str, Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name

    staff = auto()
    client = auto()
    company = auto()


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


class LoanStatusEnum(str, Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name

    created = auto()
    confirmed = auto()
    issued = auto()
    redeemed = auto()
    overdue = auto()


class LoanTypeEnum(str, Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name

    installment = auto()
    credit = auto()


class LogTypeEnum(str, Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name

    error = auto()
    warning = auto()
    ingo = auto()


class ClientSexEnum(str, Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name


    male = auto()
    female = auto()


class DocumentTypeEnum(str, Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name

    passport = auto()
    residence = auto()
    permit = auto()


class StaffRoleModel(BaseModel):
    id: Optional[int]
    staff_role_name: Optional[str]


class StaffModel(BaseModel):
    id: Optional[int]
    user_id: Optional[int]  # FK for User
    staff_role_id: Optional[int]  # FK for Staff Role


class LogsModel(BaseModel):
    id: Optional[int]
    user_id: Optional[int]  # FK for User
    staff_role_id: Optional[int]  # FK for Staff Role
    log_type: Optional[LogTypeEnum]
    log_message: Optional[str]
    time_stamp: Optional[datetime]


class CountryModel(BaseModel):
    id: Optional[int]
    country_name: Optional[str]


class CityModel(BaseModel):
    id: Optional[int]
    city_name: Optional[str]


class CitizenshipModel(BaseModel):
    id: Optional[int]
    citizenship_name: Optional[str]


class DocumentModel(BaseModel):
    id: Optional[int]
    citizenship_id: Optional[int]  # FK for Citizenship
    current_type: Optional[DocumentTypeEnum]
    documents_number: Optional[str]
    issue_date: Optional[datetime]
    expiration_date: Optional[datetime]


class ClientModel(BaseModel):
    id: Optional[Optional[int]]
    user_id: Optional[Optional[int]]  # FK for User
    country_id: Optional[Optional[int]]  # FK for Country
    city_id: Optional[Optional[int]]  # FK for City
    document_id: Optional[Optional[int]]  # FK for Document
    last_name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]
    sex: Optional[ClientSexEnum]
    birth_date: Optional[date]
    phone: Optional[str]
    address: Optional[str]


class CompanyModel(BaseModel):
    id: Optional[int]
    user_id: Optional[int]  # FK for User
    company_name: Optional[str]
    short_name: Optional[str]


class ProductTypeModel(BaseModel):
    id: Optional[int]
    product_type_name: Optional[str]


class ProductModel(BaseModel):
    id: Optional[int]
    company_id: Optional[int]  # FK for Company
    product_type_id: Optional[int]  # FK for Product Type
    product_name: Optional[str]
    product_cost: Optional[Decimal]
    product_amount: Optional[int]


class LoansModel(BaseModel):
    id: Optional[int]
    client_id: Optional[int]  # FK for Client
    company_id: Optional[int]  # FK for Company
    product_id: Optional[int]  # FK for Product
    loan_status: Optional[LoanStatusEnum]
    loan_type: Optional[LoanTypeEnum]
    order_amount: Optional[int]
    credit_period: Optional[Optional[int]]
    credit_rate: Optional[Decimal]
    outstanding_loan_amount: Optional[Decimal]
    credit_datetime: Optional[datetime]
    last_change_datetime: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
        use_enum_values = True
        json_encoders = {
            Decimal: lambda d: float(str(d)),
            datetime: lambda d: d.strftime('%Y-%m-%dT%H:%M:%SZ'),
        }


