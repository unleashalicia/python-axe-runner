import sys, os

path = sys.argv[1]

with open( path, 'r' ) as f:
  links = [x.strip() for x in f.read().split ('\n' )]
  for link in links:
    try:
      os.system( 'axe {} --save'.format( link ) )
      print( 'succes: {}'.format( link ) )
    except:
      print( 'failure: {}'.format( link ) )
