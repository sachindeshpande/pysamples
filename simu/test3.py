import simpy


class School:
    def __init__(self, env):
        self.env = env
        self.class_ends = env.event()
        self.pupil_procs = [env.process(self.pupil()) for i in range(3)]
        self.bell_proc = env.process(self.bell())

    def bell(self):
        print('In bell')
        for i in range(2):
            print('In bell loop')
            yield self.env.timeout(2)
            print('In bell loop : After timeout')
            self.class_ends.succeed()
            print('In bell loop : After succeed')
            self.class_ends = self.env.event()
            print('In bell loop : After end')
            print()

    def pupil(self):
        print('In pupil')
        for i in range(2):
            print(' \o/')
            yield self.class_ends
            print('In pupil : After yield')

env = simpy.Environment()
school = School(env)
env.run()