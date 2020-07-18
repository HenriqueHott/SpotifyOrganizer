import model.error.err as err
import statistics
import pandas as pd

class Metadata():
    def __init__(self):
        self.music_id = int
        self.danceability = float
        self.energy = float
        self.loudness = float
        self.speechiness = float
        self.acousticness = float
        self.instrumentalness = float
        self.liveness = float
        self.valence = float
        self.tempo = float
        self.duration_ms = float

    def CreateMetadata(self, data: {}):
        self.music_id = data['id']
        self.danceability = float("{:.3f}".format(data['danceability']))
        self.energy = float("{:.3f}".format(data['energy']))
        self.loudness = float("{:.3f}".format(data['loudness']))
        self.speechiness = float("{:.3f}".format(data['speechiness']))
        self.acousticness = float("{:.3f}".format(data['acousticness']))
        self.instrumentalness = float("{:.3f}".format(data['instrumentalness']))
        self.liveness = float("{:.3f}".format(data['liveness']))
        self.valence = float("{:.3f}".format(data['valence']))
        self.tempo = float("{:.3f}".format(data['tempo']))
        self.duration_ms = float("{:.3f}".format(data['duration_ms']))
        
    def CreateJSON(self) -> {}:
        a = None
        
class MetadataList():
    """ Class to list metadata information in a Pandas DataFrame"""
    def __init__(self) -> None:
      self.fields= [
        'music_id',
        'danceability',
        'energy',
        'loudness',
        'speechiness',
        'acousticness'
        'instrumentalness',
        'liveness',
        'valence',
        'tempo',
        'duration_ms',
      ]

    self.metadataFrame = pd.DataFrame(columns=self.fields)

        
    def Add(self, meta: Metadata) -> None:
        self.metadataFrame = self.metadataFrame.append(
            pd.Series([
                meta.music_id,
                meta.danceability,
                meta.energy,
                meta.speechiness,
                meta.acousticness,
                meta.instrumentalness,
                meta.liveness,
                meta.valence,
                meta.tempo,
                meta.duration_ms
                
            ], index=self.fields)
        )
        
    def Get(self, index: int) -> tuple(Metadata, err.Error):
        if index < 0:
            return Metadata(), err.Error('Invalid index')
        
        if index >= len(list(self.metadataFrame.index)):
            return Metadata(), err.Error('Null list or length smaller than the index requested')
        
        row = self.metadataFrame.iloc[index]
        meta.music_id = row['music_id']
        meta.danceability = row['danceability']
        meta.energy = row['energy']
        meta.loudness = row['loudness']
        meta.speechiness = row['speechiness']
        meta.acousticness = row['acousticness']
        meta.instrumentalness = row['instrumentalness']
        meta.liveness = row['liveness']
        meta.valence = row['valence']
        meta.tempo = row['tempo']
        meta.duration_ms = row['']
        
        return meta, None
    
    def GetByMusicID(self, music_id: int) -> tuple(Metadata, err.Error):
        indexes = self.metadataFrame.index[self.metadataFrame['music_id']].tolist()

        if indexes > 0:
            return self.Get(indexes[0])
        
        return Metadata(), err.Error('Music metadata was not found')
        
    def Len(self) -> int:
        return len(list(self.metadataFrame.index))
    
    def GetMedia(self) -> tuple(Metadata, err.Error):
        if len(list(self.metadataFrame.index)) == 0:
            return None, err.Error('Null list')
        
        # Fazer sistema de rankeamento, pegar o TIPO da musica
        # Desvio Padrão
        metadata = Metadata()
        metadata.danceability = float("{:.3f}".format(statistics.fmean(self.danceability_list)))
        metadata.energy = float("{:.3f}".format(statistics.fmean(self.energy_list)))
        metadata.loudness = float("{:.3f}".format(statistics.fmean(self.loudness_list)))
        metadata.speechiness = float("{:.3f}".format(statistics.fmean(self.speechiness_list)))
        metadata.acousticness = float("{:.3f}".format(statistics.fmean(self.acousticness_list)))
        metadata.instrumentalness = float("{:.3f}".format(statistics.fmean(self.instrumentalness_list)))
        metadata.liveness = float("{:.3f}".format(statistics.fmean(self.liveness_list)))
        metadata.valence = float("{:.3f}".format(statistics.fmean(self.valence_list)))
        metadata.tempo = float("{:.3f}".format(statistics.fmean(self.tempo_list)))
        metadata.duration_ms = float("{:.3f}".format(statistics.fmean(self.duration_ms_list)))
        
        return metadata, None
    
    def getDP(self) -> tuple(Metadata, err.Error):
        if self.music_id_list is None or len(self.music_id_list) == 0:
            return None, err.Error('Null list')
        
        # Fazer sistema de rankeamento, pegar o TIPO da musica
        # Desvio Padrão
        
        metadata = Metadata()
        metadata.danceability = float("{:.3f}".format(statistics.pstdev(self.danceability_list)))
        metadata.energy = float("{:.3f}".format(statistics.pstdev(self.energy_list)))
        metadata.loudness = float("{:.3f}".format(statistics.pstdev(self.loudness_list)))
        metadata.speechiness = float("{:.3f}".format(statistics.pstdev(self.speechiness_list)))
        metadata.acousticness = float("{:.3f}".format(statistics.pstdev(self.acousticness_list)))
        metadata.instrumentalness = float("{:.3f}".format(statistics.pstdev(self.instrumentalness_list)))
        metadata.liveness = float("{:.3f}".format(statistics.pstdev(self.liveness_list)))
        metadata.valence = float("{:.3f}".format(statistics.pstdev(self.valence_list)))
        metadata.tempo = float("{:.3f}".format(statistics.pstdev(self.tempo_list)))
        metadata.duration_ms = float("{:.3f}".format(statistics.pstdev(self.duration_ms_list)))
        
        return metadata, None
    
    def Sort(self) -> None:
        self.metadataFrame.sort_values(by='', kind='quicksort')