parents, babies = (1,1)
while babies < 100:
	print 'this generation has {0} babies'.format (babies)
	parents, babies = (babies, parents + babies)
