from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


class Renderer(ABC):
    @abstractmethod
    def render(self, data: dict) -> str:
        pass


class HTMLRenderer(Renderer):
    def render(self, data: dict) -> str:
        html = "<html><body>\n"
        for key, value in data.items():
            html += f"<p><b>{key}:</b> {value}</p>\n"
        html += "</body></html>"
        return html


class JsonRenderer(Renderer):
    def render(self, data: dict) -> str:
        return json.dumps(data, indent=4, ensure_ascii=False)


class XmlRenderer(Renderer):
    def render(self, data: dict) -> str:
        root = ET.Element("Page")
        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        return ET.tostring(root, encoding="unicode")


class Page(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def render(self) -> str:
        pass


class SimplePage(Page):
    def __init__(self, renderer: Renderer, title: str, content: str):
        super().__init__(renderer)
        self.title = title
        self.content = content

    def render(self) -> str:
        data = {
            "title": self.title,
            "content": self.content
        }
        return self.renderer.render(data)


class Product:
    def __init__(self, id: int, name: str, description: str, image: str):
        self.id = id
        self.name = name
        self.description = description
        self.image = image


class ProductPage(Page):
    def __init__(self, renderer: Renderer, product: Product):
        super().__init__(renderer)
        self.product = product

    def render(self) -> str:
        data = {
            "id": self.product.id,
            "name": self.product.name,
            "description": self.product.description,
            "image": self.product.image
        }
        return self.renderer.render(data)


if __name__ == "__main__":
    html = HTMLRenderer()
    json_r = JsonRenderer()
    xml_r = XmlRenderer()


    simple_page = SimplePage(html, "Welcome", "This is work")
    print(simple_page.render(), "\n")

    simple_page_json = SimplePage(json_r, "Welcome", "This is work")
    print(simple_page_json.render(), "\n")

    product = Product(101, "Dog", "Powerful dog", "dog.png")
    product_page_html = ProductPage(html, product)
    print(product_page_html.render(), "\n")

    product_page_xml = ProductPage(xml_r, product)
    print(product_page_xml.render())
