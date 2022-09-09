import test_pb2

field_options1 = test_pb2.FieldOptions(name='foo', options=['a', 'b'])
print(field_options1)

field_options2 = test_pb2.FieldOptions(name='bar', options=['x', 'y', 'z'])
print(field_options2)

output = test_pb2.ConfigOptions()

for x in [field_options1, field_options2]:
    output.config_options.append(x)

print(output)


# output:

# name: "foo"
# options: "a"
# options: "b"

# name: "bar"
# options: "x"
# options: "y"
# options: "z"

# config_options {
#   name: "foo"
#   options: "a"
#   options: "b"
# }
# config_options {
#   name: "bar"
#   options: "x"
#   options: "y"
#   options: "z"
# }
