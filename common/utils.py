def check_base_class_by_name(obj, base_name):
	bases = obj.__class__.__bases__ + (obj.__class__,)
	print base_name, bases
	for cls in bases:
		if cls.__name__ == base_name:
			return True
	return False