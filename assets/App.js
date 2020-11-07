import React, { Component } from 'react';
import { songList, playList } from './Constant';
import Headers from './components/Headers';
import MenuBar from './components/MenuBar';
import SongList from './components/SongList';
import PlayList from './components/Playlist';
import Paginations from './components/Paginations'
import CreatePlaylist from './components/popups/CreatePlaylist';

export class App extends Component {
  constructor(){
    super();
    this.state = {
      activeMenu:'home',
      songloader: false,
      showPlayListSong: false,
      songList: songList,
      playListSongs: {
        2345452:songList
      },
      selectedPlayList:'',
      playLists: playList,
      createPlaylist: false
    }
  }

  handleMenu(menu) {
    this.setState({
      activeMenu: menu,
      showPlayListSong: false
    })
  }

  goBackToPlaylist() {
    this.setState({
      showPlayListSong: false
    })
  }
  showPlayListSong(id, showSongs) {
    this.setState({
      selectedPlayList: id,
      showPlayListSong: showSongs
    });
  }

  deletePlayList(id) {
    let listOfPlayList  = this.state.playLists;
    let playList = listOfPlayList.filter(list => list.id !== id)
    this.setState({
      playLists: playList
    });
  }

  showCreatePlaylist(show){
    this.setState({
      createPlaylist: show
    })
  }

  addPlayList(name) {
    let listOfPlayList  = [...this.state.playLists];
    let newPlayList = {
      id:'2345453',
      name: name,
      created_date: "24/7/2020"
    }
    listOfPlayList.push(newPlayList)
    this.setState({
      playLists: listOfPlayList,
      createPlaylist: false
    });
  }

  searchSongs(search) {
    console.log(search)
  }

  render() {
    let{
      activeMenu,
      showPlayListSong,
      playLists,
      songloader,
      songList,
      playListSongs,
      selectedPlayList,
      createPlaylist
    } = this.state;

    songList = showPlayListSong ? playListSongs[selectedPlayList]: songList; 

    return (
      <div className="music-app">
        <Headers />
        <div className="music-components">
          <MenuBar 
            activeMenu={activeMenu } 
            handleMenu={this.handleMenu.bind(this)}
            searchSongs={this.searchSongs.bind(this)}
          />
          {
            activeMenu === 'playList' && !showPlayListSong?
            <PlayList 
              playLists={playLists}
              showPlayListSong={this.showPlayListSong.bind(this)}
              deletePlayList={this.deletePlayList.bind(this)}
              showCreatePlaylist={this.showCreatePlaylist.bind(this)}
            /> 
            : 
            songList.length>=1&&
            <SongList 
              songloader={songloader} 
              songList={songList}
              showPlayListSong={showPlayListSong}
              goBackToPlaylist={this.goBackToPlaylist.bind(this)}
            />
          }
          {activeMenu !== 'playList' && songList.length >= 1 &&
          <Paginations />
        }
        </div>
        <CreatePlaylist 
          createPlaylist={createPlaylist}
          showCreatePlaylist={this.showCreatePlaylist.bind(this)}
          addPlayList={this.addPlayList.bind(this)}
        />
      </div>
    )
  }
}
export default App;
