# README

## Set-up:
1. Create the environment. You only need to do this once, but make sure to do this for each unique environment version. \
  `conda env create -f doclue_env.yml -n doclue_env`
2. List environments to make sure it has been created. \
  `conda env list` or `conda info --envs` 
3. Activate the environment. \
  `conda activate doclue_env`

## Run the game:

On your main directory, run `start.py` or `python3 start.py`

## Run multi-player game:

**make sure your own computer IP is in the code so that it can be run**

Open multiple terminals
1 terminal for the server/splash screen
    run `clueless\Server.py`
    to exit, must kill the terminal (TODO: exit by keyboard shortcut)
3-6 terminals for players
    run `start.py` in each
    to exit, close out the client window

## Pickling Custom Objects:
The `clueless/logs/` folder currently stores the files we write our objects to during the preparation to pickle and send an object. We can decide later if we want to continuously overwrite one file, or write new files for each object state send-off.

1. To send an object
  `logs_folder = Path("clueless/logs/")`
  #create object
  `test_player = Player(name='plum', pos_x=0, pos_y=0, width=0, height=0, color='red')`
  #create a pickle file
  `picklefile = open(f'{logs_folder}/player_test', 'wb')`
  #pickle the dictionary and write it to file
  `pickle.dump(test_player, picklefile)`
  #close the file
  `picklefile.close()`

2. To receive an object
  #read the pickle file
  `read_player_file = open(f'{logs_folder}/player_test', 'rb')`
  #unpickle the dataframe
  `read_player = pickle.load(read_player_file)`
  #close file
  `read_player_file.close()`

3. To read an object
  #print the object type 
  `print(type(read_player))`
  #print the object attribute, name
  `print(read_player.player_name)`

