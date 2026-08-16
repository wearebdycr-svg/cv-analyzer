from pydantic import BaseModel, Field

class AnalisisCV(BaseModel):
    """Modelo de datos para el analisis completo de un CV."""
    
    nombre_candidato: str = Field(description = "Nombre completo del candidato extraido del CV.")
    experiencia_años: int = Field(description = "Años totales de experiencia laboral relevante.")
    habilidades_clave: list[str] = Field(description = "Lista de las 5-7 habilidades del candidato mas relevantes para el puesto.")
    education: str = Field(description = "Nicel educativo mas alto y especializacion principal.")
    experiencia_relevante: str = Field(description = "Resumen consiso de la experiencia mas relevante para el puesto expesifico.")
    fortalezas: list[str] = Field(description = "3-5 principales fortalezas del candidato basadas en su perfil.")
    areas_mejora: list[str] = Field(description = "2-4 areas donde el candidato podria desarrollarse o mejorar.")
    porcentaje_ajuste: int = Field(description = "Porcentaje de ajuste al puesto (0-100) basado en experiencia, habilidades y formacion.", ge = 0, le = 100)