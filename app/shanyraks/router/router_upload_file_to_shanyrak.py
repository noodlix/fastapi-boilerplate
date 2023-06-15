from fastapi import Depends, UploadFile
from typing import List

from ..service import Service, get_service
from . import router


@router.post("/file")
def upload_file(
    file: UploadFile,
    svc: Service = Depends(get_service),
):
    """
    file.filename: str - Название файла
    file.file: BytesIO - Содержимое файла
    """
    url = svc.s3_service.upload_file(file.file, file.filename)

    return {"msg": url}


@router.patch("/{shanyrak_id:str}/media")
def upload_files(
    files: List[UploadFile],
    svc: Service = Depends(get_service),
):

    result = []
    for file in files:
        url = svc.s3_service.upload_file(file.file, file.filename)
        result.append(url)

    return {"msg": files}
