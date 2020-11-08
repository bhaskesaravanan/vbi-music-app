import React, { Component } from 'react';
import { songList, playList } from './constant';
import * as apis from './Api';
import Headers from './components/Headers';
import MenuBar from './components/MenuBar';
import SongList from './components/SongList';
import PlayList from './components/Playlist';
import Paginations from './components/Paginations'
import CreatePlaylist from './components/popups/CreatePlaylist';
import PlayListModel from './components/popups/PlayListModel';
import LoginPopup from './components/popups/LoginPopup';

export class App extends Component {
  constructor(){
    super();
    this.state = {
      activeMenu:'home',
      songloader: false,
      showPlayListSong: false,
      songList: [],
      playListSongs: {},
      selectedPlayList:'',
      playLists: [],
      createPlaylist: false,
      search: false,
      showPlayListModel: false,
      songId: '',
      songOffset: 1,
      loginPopup: false,
      isLogin: false

    }
  }

  async componentDidMount() {
    let songList = await this.fetchSongs();
    this.setState({
      songList
    })
  }

  async handleMenu(menu) {
    await this.fetchPlayList();
    this.setState({
      activeMenu: menu,
      showPlayListSong: false
    })
  }

  async fetchPlayList() {
    let playListResponse = await apis.fetchPlayList(window.user_id);
    if(!playListResponse || !playListResponse.success) 
      return this.setState({
        playLists: []
      });
    let playLists = playListResponse.playlists;
    this.setState({
      playLists
    });
  };

  goBackToPlaylist() {
    this.setState({
      showPlayListSong: false,
      selectedPlayList: '',
      search: false
    })
  }

  async showPlayListSong(id, showSongs) {
    let playListSongs = this.state.playListSongs
    if(!Object.keys(playListSongs).length || !playListSongs[id]) {
      let songList = await this.fetchSongs(id);
      playListSongs[id] = songList
    }
    this.setState({
      playListSongs: playListSongs,
      selectedPlayList: id,
      showPlayListSong: showSongs
    });
  }

  async fetchSongs(playlistId=this.state.selectedPlayList) {
    let songListResponse = await apis.fetchSongs(playlistId);
    if(!songListResponse || !songListResponse.success) 
      return []
    let songList = songListResponse.song_list;
    return songList
  }

  async deletePlayList(id) {
    let listOfPlayList  = this.state.playLists;
    let payload = {
      'user_id': window.user_id,
      'playlist_id': id
    }
    let playListResponse = await apis.deletePlayList(payload);
    if(!playListResponse || !playListResponse.success) {
      console.log('playlist add failed')
      return 
    }
    let playList = listOfPlayList.filter(list => list.id !== id)
    this.setState({
      playLists: playList
    });
  }

  showCreatePlaylist(show) {
    if(!this.state.isLogin&&!window.user_id) {
      this.showLoginPppup(true)
      return;
    }
    this.setState({
      createPlaylist: show
    })
  }

  showLoginPppup(show) {
    this.setState({
      loginPopup: show
    })
  }

  async addPlayList(name) {
    if(!this.state.isLogin&&!window.user_id) {
      this.showLoginPppup(true)
      return;
    }
    let listOfPlayList  = [...this.state.playLists];
    let payload = {
      'playlist_name': name,
      'user_id': window.user_id
    }
    let playListResponse = await apis.savePlayList(payload);
    if(!playListResponse || !playListResponse.success) {
      if(!playListResponse.login_required) {
        this.showLoginPppup(true);
        return;
      }
      console.log('playlist add failed')
      return 
    }
    let newPlayList = playListResponse.playlist;
    listOfPlayList.push(newPlayList)
    this.setState({
      playLists: listOfPlayList,
      createPlaylist: false
    });
  }

  async searchSongs(search) {
    console.log(search);
    let songList = await this.fetchSongs();
    this.setState({
      songList,
      showPlayListSong: true,
      search: true
    });
  }

  async deleteSongsFromPlaylist(songId) {
    let { playListSongs, selectedPlayList } = this.state;
    let payload = {
      'playlist_id': selectedPlayList,
      'song_id': songId,
      'user_id': window.user_id
    }
    let playListResponse = await apis.deleteSongsFromPlayList(payload);
    if(!playListResponse || !playListResponse.success) {
      console.log('song deletion failed');
      return ;
    }
    let selectedPlayListSong = playListSongs[selectedPlayList];
    let activeSongs = selectedPlayListSong.filter(song=>song.id!==songId);
    playListSongs[selectedPlayList] = activeSongs;
    this.setState({
      playListSongs
    });
  }

  async showPlayListModal(show, songId='') {
    if(!show) {
      this.setState({
        songId,
        showPlayListModel: show,
      })
    }
    else{
      if(!this.state.playLists.length) await this.fetchPlayList()
      this.setState({
        songId,
        showPlayListModel: show,
      });
    }
  }

  async addSongsToPlaylist(songId, selectedPlayList) {
    let { playListSongs, songList } = this.state;
    let payload = {
      'song_id': songId,
      'user_id': window.user_id,
      'playlist_id': selectedPlayList
    }
    let playListResponse = await apis.addSongsToPlayList(payload);
    if(!playListResponse || !playListResponse.success) {
      console.log('song deletion failed');
      return ;
    }
    let songObject = songList.filter(song => song.id===songId);
    if(!Object.keys(playListSongs).length || !playListSongs[selectedPlayList].length) {
      playListSongs[selectedPlayList] = [songObject]
    }
    else{
      playListSongs[selectedPlayList].push(songObject[0]);
    }
    this.setState({
      playListSongs,
      songId: '',
      showPlayListModel: false
    });
  }

  setPagination(page){
    this.setState({
      songOffset: page
    })
  }

  async login(payload) {
    console.log(payload)
    let loginResponse = await apis.login(payload);
    if(!loginResponse || !loginResponse.success) {
      console.log('login failed');
      return ;
    }
    window.user_id = loginResponse.user_id
    this.setState({
      loginPopup: false,
      isLogin: true
    })
  }

  async signupProcess(payload) {
    console.log(payload)
    let loginResponse = await apis.signup(payload);
    if(!loginResponse || !loginResponse.success) {
      console.log('login failed');
      return ;
    }
    this.setState({
      loginPopup: false,
      isLogin: true
    })
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
      createPlaylist,
      search,
      showPlayListModel,
      songId,
      songOffset,
      loginPopup
    } = this.state;

    songList = showPlayListSong && !search ? playListSongs[selectedPlayList]: songList; 

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
              songOffset={songOffset}
              songloader={songloader} 
              songList={songList}
              showPlayListSong={showPlayListSong}
              search={search}
              goBackToPlaylist={this.goBackToPlaylist.bind(this)}
              deleteSongsFromPlaylist={this.deleteSongsFromPlaylist.bind(this)}
              showPlayListModal={this.showPlayListModal.bind(this)}
            />
          }
          {activeMenu !== 'playList' && songList.length >= 1 &&
          <Paginations setPagination={this.setPagination.bind(this)} />
        }
        </div>
        <CreatePlaylist 
          createPlaylist={createPlaylist}
          showCreatePlaylist={this.showCreatePlaylist.bind(this)}
          addPlayList={this.addPlayList.bind(this)}
          
        />
        <PlayListModel 
          songId={songId}
          playLists={playLists}
          showPlayListModel={showPlayListModel}
          showPlayListModal={this.showPlayListModal.bind(this)}
          addSongsToPlaylist={this.addSongsToPlaylist.bind(this)}
        />
        <LoginPopup 
          loginPopup={loginPopup} 
          showLoginPppup={this.showLoginPppup.bind(this)}
          signupProcess={this.signupProcess.bind(this)}
          login={this.login.bind(this)}
        />
      </div>
    )
  }
}
export default App;
