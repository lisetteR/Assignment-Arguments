# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greeting_template= 'Hello, <name>!'):
    greeting_template = greeting_template.replace('<name>', name)
    return greeting_template
print(greet('Bob'))
print(greet('Yo', "What's up, <name>!"))


def force(mass: float, body:str = 'earth'):
    implementation = {
        'sun': 274.0,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
        }

    x = mass * (implementation[body])
    return x
print(force(10.0, 'saturn'))

def pull(m1: float, m2: float, d:float):
    G = 6.674*10**-11
    x = G*((m1*m2)/d**2)
    return x

print(pull(0.1, 5.972*10**24, 6.371*10**6))