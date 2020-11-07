import React from 'react'
import { Segment } from 'semantic-ui-react';
import { Header, Table, Icon } from 'semantic-ui-react'


function SongList(props) {
    return (
        <Segment className="music-segment" attached="bottom" loading={props.songloader}>
            {props.showPlayListSong && 
                <a href="#"style={{
                    'color': "black",
                    'fontSize': "medium"
                }}
                onClick={()=>props.goBackToPlaylist()}
                >
                    <Icon name="arrow left" size="large" color="black"/>
                    Back
                </a>
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
                            props.songList.map(
                                (song, index) =>{
                                    return(
                                    <Table.Row key={index}>
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
                                            {props.showPlayListSong&&
                                            <Table.Cell>
                                                <Icon name='close' />
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
