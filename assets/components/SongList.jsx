import React, {useState, useEffect} from 'react'
import { Segment } from 'semantic-ui-react';
import { Header, Table, Icon, Button } from 'semantic-ui-react'


function SongList(props) {
    const [visibleSong, setVisibleSong] = useState([])
    useEffect(() => {
        let totalSongs = (props.songOffset * 7) - 1;
        let startIndex = totalSongs - 7;
        let endIndex = totalSongs;
        let songs = props.songList.filter((song,index)=>
            index>=startIndex && index<=endIndex
        );
        setVisibleSong(songs)
    }, [props.songOffset])

    function shuffleSongs() {
        let songList = [...visibleSong];

        for (let i = songList.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [songList[i], songList[j]] = [songList[j], songList[i]];
        }
    setVisibleSong(songList)
    }

    return (
        <Segment className="music-segment" attached="bottom" loading={props.songloader}>
            {props.showPlayListSong && 
                <React.Fragment>
                <a href="#"style={{
                    'color': "black",
                    'fontSize': "medium"
                }}
                onClick={()=>props.goBackToPlaylist()}
                >
                    <Icon name="arrow left" size="large" color="black"/>
                    Back
                </a>
                <div className ="shuffle-btn">
                    <Button 
                        animated 
                        floated="right" 
                        className="add-playlist" 
                        color="blue"
                        onClick={()=>shuffleSongs()}
                    >
                        <Button.Content visible>Shuffle Playlist</Button.Content>
                        <Button.Content hidden>
                            <Icon name='shuffle' />
                        </Button.Content>
                    </Button>
                 </div>
                
                </React.Fragment>

                
            }

            <div className="song-list">
                <Table basic='very' celled collapsing>
                    <Table.Header>
                    <Table.Row>
                    <Table.HeaderCell>#</Table.HeaderCell>
                        <Table.HeaderCell>TITLE</Table.HeaderCell>
                    <Table.HeaderCell>ARTIST</Table.HeaderCell>
                        <Table.HeaderCell>DURATION</Table.HeaderCell>
                        {props.showPlayListSong&&<Table.HeaderCell> </Table.HeaderCell>}
                    </Table.Row>
                    </Table.Header>

                    <Table.Body>
                        {
                            visibleSong.map(
                                (song, index) =>{
                                    return(
                                    <Table.Row key={song.id}>
                                        <Table.Cell>
                                            {index+1}
                                            </Table.Cell>
                                            <Table.Cell>
                                            <Header as='h4' image>
                                                <Header.Content>
                                                {song.title}
                                                <Header.Subheader>{song.album}</Header.Subheader>
                                                </Header.Content>
                                            </Header>
                                            </Table.Cell>
                                            <Table.Cell>{song.artist}</Table.Cell>
                                            <Table.Cell>{song.duration}</Table.Cell>
                                            {props.showPlayListSong && !props.search&&
                                                <Table.Cell onClick={()=>props.deleteSongsFromPlaylist(song.id)} style={{"cursor": "pointer"}}>
                                                    <Icon name='close' />
                                                </Table.Cell>
                                            }
                                            {props.showPlayListSong && props.search&&
                                                <Table.Cell onClick={()=>props.showPlayListModal(true, song.id)} style={{"cursor": "pointer"}}>
                                                    <Icon name='music' />
                                                </Table.Cell>
                                            }
                                    </Table.Row>
                                    )
                                }
                            )
                        }
                    </Table.Body>
                </Table>
            </div>
        </Segment>  
   )
}

export default SongList;
