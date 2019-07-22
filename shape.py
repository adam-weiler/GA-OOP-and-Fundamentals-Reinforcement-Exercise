def draw_shape(options):
  shape = ""

  for r in range(options['rows']):
    for c in range(options['cols']):
      shape += options['char']

    shape += "\n"

  return shape

print(draw_shape({'cols':4,'rows':4,'char':'*'}))

print(draw_shape({'cols':9,'rows':3,'char':'0'}))