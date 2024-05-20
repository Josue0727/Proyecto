import reflex as rx
from reflex import event

class ClaveState(rx.State):
    state: int = 0

    def handle_yes(self):
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 2
        elif self.state == 2:
            self.state = 4
        elif self.state == 3:
            self.state = 5
        elif self.state == 4:
            self.state = 7
        elif self.state == 5:
            self.state = 9

    def handle_no(self):
        if self.state == 0:
            self.state = 3
        elif self.state == 1:
            self.state = 6
        elif self.state == 2:
            self.state = 5
        elif self.state == 3:
            self.state = 8
        elif self.state == 4:
            self.state = 8

def clave_page() -> rx.Component:
    return rx.cond(
        ClaveState.state == 0,
        rx.vstack(
            rx.text("MADERA PESADA"),
            rx.text("1. Sin parénquima axial aliforme?"),
            rx.button("Sí", on_click=ClaveState.handle_yes),
            rx.button("No", on_click=ClaveState.handle_no),
        ),
        rx.cond(
            ClaveState.state == 1,
            rx.vstack(
                rx.text("2. Madera moderadamente dura con parénquima axial paratraqueal unilateral y en bandas marginales discontinuas, porosidad difusa, con poros medianos de notoria disposición dendrítica y otros sin disposición. Agrupación de poros en múltiplos radiales cortos, por lo general sin agrupación. Presencia de gomas amarillas y tilides, con radios medianos?"),
                rx.button("Sí", on_click=ClaveState.handle_yes),
                rx.button("No", on_click=ClaveState.handle_no),
            ),
            rx.cond(
                ClaveState.state == 2,
                rx.vstack(
                    rx.text("Caryodanopsis Sp (Yumbé)"),
                ),
                rx.cond(
                    ClaveState.state == 3,
                    rx.vstack(
                        rx.text("1'. Parénquima axial aliforme confluente con ala ancha y paratraqueal vasicéntrico abundante. Poros sin disposición, con porosidad difusa de tamaño mediano, solitarios o con múltiplos radiales cortos y algunas veces largos. Contenido en gomas, sin parénquima apotraqueal, radios medianos."),
                        rx.button("Sí", on_click=ClaveState.handle_yes),
                        rx.button("No", on_click=ClaveState.handle_no),
                    ),
                    rx.cond(
                        ClaveState.state == 4,
                        rx.vstack(
                            rx.text("MADERA MEDIANAMENTE PESADA"),
                            rx.text("1. Parénquima axial paratraqueal vasicéntrico escaso a muy escaso, porosidad difusa con poros medianos sin disposición y sin agrupación o rara vez con múltiplos radiales cortos, contenido en gomas oscuras, con parénquima apotraqueal en agregados?"),
                            rx.button("Sí", on_click=ClaveState.handle_yes),
                            rx.button("No", on_click=ClaveState.handle_no),
                        ),
                        rx.cond(
                            ClaveState.state == 5,
                            rx.vstack(
                                rx.text("2'. Madera dura, parénquima paratraqueal vasicéntrico abundante, y en bandas marginal, porosidad difusa, con poros medianos, con porosidad dendrítica rara vez mayormente sin disposición, poros solitarios y rara vez múltiplos radiales cortos. Presencia de esclerotílides, con floema incluido. Radios finos?"),
                                rx.button("Sí", on_click=ClaveState.handle_yes),
                                rx.button("No", on_click=ClaveState.handle_no),
                            ),
                            rx.cond(
                                ClaveState.state == 6,
                                rx.vstack(
                                    rx.text("Clathrotropis Sp. (Sapán)"),
                                ),
                                rx.cond(
                                    ClaveState.state == 7,
                                    rx.vstack(
                                        rx.text("Hieronyma Sp."),
                                    ),
                                    rx.cond(
                                        ClaveState.state == 8,
                                        rx.vstack(
                                            rx.text("Chipa"),
                                        ),
                                        rx.cond(
                                            ClaveState.state == 9,
                                            rx.vstack(
                                                rx.text("Anacardium Sp (Caracolí)"),
                                            ),
                                            rx.vstack(
                                                rx.text("Clave dicotómica completa"),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )

if __name__ == "__main__":
    app = rx.App()
    app.add_page(clave_page, title="Clave", state=ClaveState)
    app.run()

