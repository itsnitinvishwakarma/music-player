
# model file assignment

def add_song(self, song_name, song_path):
    self.song_dict[song_name] = song_path
    print("song added:", self.song_dict[song_name])


def get_song_path(self, song_name):
    return self.song_dict[song_name]


def remove_song(self, song_name):
    self.song_dict.pop(song_name)
    print(self.song_dict)


def remove_song_from_favourites(self,song_name):
    self.cur.execute("Delete from myfavourites where song_name=:1",(song_name,))
    if self.cur.rowcount==0:
        return "song not present in ur favourites"

    self.conn.commit()
    self.song_dict.pop(song_name)
    return "song deleted from ur favourites"

#  player file assign

    def stop_song(self):
        mixer.music.stop()

    def pause_song(self):
        mixer.music.pause()

    def unpause_song(self):
        mixer.music.unpause()

    def add_song_to_favourites(self,song_name):
        #my written codes
        song_path=self.my_model.get_song_path(song_name)
        add_status=self.my_model.add_song_to_favourites(song_name,song_path)
        return add_status


    def load_songs_from_favourites(self):
        # my written codes
        load_status=self.my_model.load_songs_from_favourites()
        return load_status,self.my_model.song_dict


    def remove_song_from_favourites(self,song_name):
        # my written codes
        remove_song_status=self.my_model.remove_song_from_favourites(song_name)
        return remove_song_status

#    view file assign

    def change_volume(self,val):
        volume_level = float(val)/100
        self.my_player.set_volume(volume_level)

    def show_song_details(self):
        self.song_length = self.my_player.get_song_length(self.song_name)
        minutes=self.song_length/60
        seconds=self.song_length%60
        self.songTotalDuration.configure(text=str(minutes)+":"+str(seconds))

        self.songTimePassed.configure(text='0:0')
        if len(self.songName)>14:
            self.songName.configure(text=self.songName[0:14]+"...")
        else:
            self.songName.configure(text=self.songName)


    def list_double_click(self,e):
        self.play_song()



    def stop_song(self):
        self.my_player.stop_song()
        self.isPlaying = False



    def pause_song(self):
        if self.isPlaying:
            if self.isPaused == False:
                self.my_player.pause_song()
                self.isPaused = True
            else:
                self.my_player.unpause_song()
                self.isPaused = False

    def load_previous_song(self):
            # OR my written code

        if self.isPlaying == False:
            messagebox.showerror("error","plz first play a song")
            self.i=self.i+1
            self.cur_song_index = self.playList.curselection()
            if self.i <= self.cur_song_index[0]:
                self.song_name = self.playList.get(self.cur_song_index[0]-self.i)
            else:
                self.song_name = self.playList.get(tk.END)
                self.i=0
            self.show_song_details()
            self.my_player.play_song()
            self.change_volume(self.vol_scale.get())


    def remove_song_from_favourites(self):
        fav_song_index_tuple = self.playList.curselection()
        try:
            if len(fav_song_index_tuple) == 0:
                raise NoSongSelectedError("plz select a song to delete from favourites")
            song_name = self.playList.get(fav_song_index_tuple[0])
            remove_song_status=self.my_player.remove_song_from_favourites(song_name)
            messagebox.showinfo("deleted",remove_song_status)
        except(NoSongSelectedError)as ex1:
            messagebox.showerror("Error!", ex1)
            print(ex1)
