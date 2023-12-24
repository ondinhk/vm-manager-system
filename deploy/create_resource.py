import csv

from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader('templates'))


def generate_resource(template_dir, output_dir, list_data):
    template = template_env.get_template(template_dir)
    rendered = template.render(list_data=list_data)
    with open(output_dir, 'w') as output_file:
        output_file.write(rendered)
    print(f"Render success {output_dir}")


def csv_to_dict(csv_file_path):
    result_dict_list = []
    with open(csv_file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result_dict_list.append(row)
    return result_dict_list


if __name__ == '__main__':
    data = csv_to_dict('./templates/data.csv')
    generate_resource(template_dir='deployments.jinja', output_dir='./helm-chart/worker-chart/templates/deployments.yaml', list_data=data)
    generate_resource(template_dir='services.jinja', output_dir='./helm-chart/worker-chart/templates/services.yaml', list_data=data)
    generate_resource(template_dir='ingress.jinja', output_dir='./helm-chart/worker-chart/templates/ingress.yaml', list_data=data)