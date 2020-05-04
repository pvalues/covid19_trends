## helper functions
#isUnique function
def isUnique(df, lst):
	"""
	this function returns a boolean check on uniqueness
	of a Pandas DF in specified column list
	"""
	return (len(df.drop_duplicates(subset=lst)) == len(df))
