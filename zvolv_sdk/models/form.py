from pydantic import BaseModel
from typing import List, Optional, Union, Any


class Element(BaseModel):
    id: Optional[str] = None
    elementId: Optional[str] = None
    label: Optional[str] = None
    type: Optional[str] = None
    defaultValue: Optional[Union[str, bool, int, dict, list]] = None
    required: Optional[bool] = False
    disabled: Optional[bool] = False
    hidden: Optional[bool] = False
    unique: Optional[bool] = False
    updateIfUnique: Optional[bool] = False
    properties: Optional[dict] = {}
    attributes: Optional[dict] = {}
    dependencies: Optional[List[Any]] = []
    validations: Optional[List[Any]] = []
    dataType: Optional[str] = None
    rbacConf: Optional[dict] = {}
    abacConf: Optional[dict] = {}
    showLabel: Optional[bool] = True


class Form(BaseModel):
    id: Optional[str] = None
    uuid: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    type: Optional[str] = None
    schemaVersion: Optional[str] = None
    allowDraft: Optional[bool] = False
    setDraftInterval: Optional[int] = None
    allowDraftNotPassed: Optional[bool] = False
    enableRetrofit: Optional[bool] = True
    enableReSync: Optional[bool] = True
    abacOperator: Optional[str] = None
    tags: Optional[List[str]] = []
    canReadRoles: Optional[List[Any]] = []
    canUpdateRoles: Optional[List[Any]] = []
    configurations: Optional[dict] = {}
    elements: List[Element] = []
