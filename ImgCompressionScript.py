from PIL import Image
from os import listdir

input_folder  = 'C:\\Users\\alessandro.silva\\Desktop\\PCM\\fotos manutenção\\'
output_folder = 'C:\\Users\\alessandro.silva\\Desktop\\PCM\\fotos manutenção\\'

def open_and_compress( input_path: str, output_path: str, max_size: int = 640 ) -> None:
    "Opens image in the input path, compresses it, converts it to jpg and saves it to the output path."
    with Image.open( input_path ) as img:
        width, height = img.size
        if max( height, width ) <= max_size:
            return None
        elif width > height:
            new_width = min( width, max_size )
            new_height = round( height * ( new_width / width ) )
        else:
            new_height = min( height, max_size )
            new_width = round( width * ( new_height / height ) )
        img = img.resize( ( new_width, new_height ) )
        img.save( output_path, format = "JPEG" )

for file in listdir( input_folder ):
    name, extension = file.rsplit( '.', 1 )
    if extension in { 'jpg', 'png' }:
        input_path  = input_folder  + file
        output_path = output_folder + name + '.jpg'
        open_and_compress( input_folder, output_folder )

