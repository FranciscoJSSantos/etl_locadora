from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import db_settings as settings


Base = declarative_base()

#Classes do banco operacional

class Artistas(Base):
    __tablename__ = 'artistas' #obrigatório
    __table_args__ = ({"schema": "locadora"})

    cod_art = Column (Integer(4), primary_key=True)
    tpo_art = Column (String(1))
    nac_bras = Column (String(1))
    cod_grav = Column (Integer(4), ForeignKey("gravadoras.cod_grav"))
    qtd_tit = Column (Integer(4))
    med_anual = Column (Float)
    nom_art = Column (String(40))
    
    def __getattribute__(self, __name: str):
        return super().__getattribute__(__name)
    
class Copias(Base):
    __tablename__ = "copias"  
    __table_args__ = ({"schema": "locadora"})
    cod_tit = Column (Integer(6),ForeignKey("titulos.cod_tit") ,primary_key=True)
    num_cop = Column (Integer(2), primary_key=True)
    dat_aq = Column (Date)
    status = Column (String(1))
    
    def __getattribute__(self, __name: str):
        return super().__getattribute__(__name)
    
class Gravadoras(Base):
    __tablename__ = "gravadoras"    
    __table_args__ = ({"schema": "locadora"})

    cod_grav = Column (Integer(4), primary_key=True)
    uf_grav = Column (String(2))
    nac_bras = Column (String(1))
    nom_grav = Column (String(40))
    
    def __getattribute__(self, __name: str):
        return super().__getattribute__(__name)
    
class ItensLocacoes(Base):
    __tablename__ = "itens_locacoes"
    __table_args__ = ({"schema": "locadora"})

    cod_soc = Column(Integer(4), ForeignKey("locacoes.cod_soc"), primary_key=True)
    dat_loc = Column(Date, ForeignKey("locacoes.dat_loc" ), primary_key=True)
    cod_tit = Column(Integer(6), ForeignKey("copias.cod_tit") , primary_key=True)
    num_cop = Column(Integer(2), ForeignKey("copias.num_cop") , primary_key=True)
    dat_prev = Column(Date)
    val_loc = Column(Float)
    sta_mul = Column(String(1))
    dat_dev = Column(Date)
    
    def __getattribute__(self, __name: str):
        return super().__getattribute__(__name)
    
class Locacoes(Base):
    __tablename__ = "locacoes"
    __table_args__ = ({"schema": "locadora"})

    cod_soc = Column(Integer(4), ForeignKey("socios.cod_soc"), primary_key=True)
    dat_loc = Column(Date, primary_key=True)
    val_loc = Column(Float)
    dat_venc = Column(Date)
    sta_pgto = Column(String(1))
    dta_pgto = Column(Date)
    
    def __getattribute__(self, __name: str):
        return super().__getattribute__(__name)
    
class Socios(Base):
    __tablename__ = "socios"
    __table_args__ = ({"schema": "locadora"})

    cod_soc = Column(Integer(4), primary_key=True)
    dat_cad = Column(Date)
    cod_tps = Column(Integer(4), ForeignKey("tipos_socios.cod_tps"))
    sta_soc = Column(String(1))
    nom_soc = Column(String(40))

    def __getattribute__(self, __name: str):
        return super().__getattribute__(__name)
    
class TiposSocios(Base):
    __tablename__ = "tipos_socios"
    __table_args__ = ({"schema": "locadora"})

    cod_tps = Column(Integer(4), primary_key=True)
    lim_tit = Column(Integer(2))
    val_base = Column(Float)
    dsc_tps = Column(String(40))

    def __getattribute__(self, __name: str):
        return super().__getattribute__(__name)
    
class Titulos(Base):
    __tablename__ = "titulos"
    __table_args__ = ({"schema": "locadora"})

    cod_tit = Column(Integer(6), primary_key=True)
    tpo_tit = Column(String(1))
    cla_tit = Column(String(1))
    qtd_cop = Column(Integer(3))
    dat_lanc = Column(Date)
    cod_art = Column(Integer(4), ForeignKey("artistas.cod_art"))
    cod_grav = Column(Integer(4), ForeignKey("gravadoras.cod_grav"))
    dsc_tit = Column(String(40))

    def __getattribute__(self, __name: str):
        return super().__getattribute__(__name)


class DM_GRAVADORA(Base):
    
    __tablename__ = 'dm_gravadora'
    __table_args__ = ({"schema": "dw_locadora"})
    
    id_grav = Column(Integer, primary_key=True)
    uf_grav = Column(String(40))
    nac_bras = Column(String(40))
    nom_grav = Column(String(40))
    
    def __init__(self, gravadoras: Gravadoras) -> None:
        super().__init__()
        self.id_grav = gravadoras.id_grav
        self.uf_grav = gravadoras.uf_grav
        self.nac_bras = gravadoras.nac_bras
        self.nom_grav = gravadoras.nom_grav

###Classes do banco dimensional


class DM_ARTISTAS(Base):
    
    __tablename__ = 'dm_artistas'
    __table_args__ = ({"schema": "dw_locadora"})
    
    id_art = Column(Integer, primary_key=True)
    tpo_art = Column(String(40))
    nac_bras = Column(String(40))
    nom_art = Column(String(40))
    
    def __init__(self, artistas : Artistas) -> None:
        super().__init__()
        self.id_art = artistas.id_art
        self.tpo_art = artistas.tpo_art
        self.nac_bras = artistas.nac_bras
        self.nom_art = artistas.nom_art





