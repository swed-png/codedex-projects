import imageio.v3 as iio

filenames = ['pokemon-gif-1.png', 'pokemon-gif-2.png', 'pokemon-gif-3.png', 'pokemon-gif-4.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('pokemon.gif', images, duration = 500, loop = 0)
