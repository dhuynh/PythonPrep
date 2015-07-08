from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "Not configured. Subclass and Implement Enter"
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		current_scene.enter()

class Failure(Scene):

	failureMessages = [
		"Pick yourself up and try again",
		"Sometimes we have bad days...",
		"They say the smartest people have high EQ. Hold Steady my friend"
	] 

	def enter(self):
		print Failure.failureMessages[randint(0, len(self.failureMessages)-1)]

class Bed(Scene):

	

class Map(object):

	scenes = {
		''
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene (self, scene_name):
		next = Map.scenes.get(scene_name)
		return next

	def opening_scene(self):
		return self.next_scene(self.start_scene)


startScene = Map('central_corridor')
game = Engine(startScene)
game.play()




