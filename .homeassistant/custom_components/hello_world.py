# domain of componenet. equal to filename

DOMAIN = "hello_world"


def setup(hass, config):
	"""Setup the hello_world component."""

	# state format:; DOMAIN.OBJECT_ID.
	hass.states.set('hello_world.Hello_World','Works!')

	#return boolean to indicate that init was successful
	return True
