import xmltodict
import numpy as np


def parse_xml(xml_path):
    """
    解析xml文件，返回标注边界框坐标
    """
    # print(xml_path)
    with open(xml_path, 'rb') as f:
        xml_dict = xmltodict.parse(f)
        # print(xml_dict)

        bndboxs = list()
        objects = xml_dict['annotation']['object']
        if isinstance(objects, list):
            for obj in objects:
                obj_name = obj['name']
                difficult = int(obj['difficult'])
                if 'car'.__eq__(obj_name) and difficult != 1:
                    bndbox = obj['bndbox']
                    bndboxs.append((int(bndbox['xmin']), int(bndbox['ymin']), int(bndbox['xmax']), int(bndbox['ymax'])))
        elif isinstance(objects, dict):
            obj_name = objects['name']
            difficult = int(objects['difficult'])
            if 'car'.__eq__(obj_name) and difficult != 1:
                bndbox = objects['bndbox']
                bndboxs.append((int(bndbox['xmin']), int(bndbox['ymin']), int(bndbox['xmax']), int(bndbox['ymax'])))
        else:
            pass

        return np.array(bndboxs)


def parse_xml_object(xml_path):
    """
    解析xml文件，返回标注对象names
    """
    with open(xml_path, 'rb') as f:
        xml_dict = xmltodict.parse(f)

        if 'object' not in xml_dict['annotation']:
            return ['Other']
        objects = xml_dict['annotation']['object']
        names = []
        if isinstance(objects, list):
            names = list(ob['name'] for ob in objects)
        else:
            names.append(objects['name'])

        return list(set(names))
