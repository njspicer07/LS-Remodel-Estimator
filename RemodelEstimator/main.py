
import tkinter as tk
from tkinter import ttk, messagebox
from calculator import calculate_estimate
from equipment import get_equipment_list


# ============================================================
# GUI
# ============================================================

class RemodelEstimator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.results_text = None

        self.title("Remodel Estimator")
        self.geometry("800x1000")
        self.minsize(700, 600)
        self.resizable(True, True)

        self.create_variables()
        self.create_widgets()


    # ========================================================
    # Tkinter Variables
    # ========================================================

    def create_variables(self):
            #measurements
        self.linfeet_var = tk.StringVar()
        self.tile_sqft_var = tk.StringVar()
        self.plaster_sqft_var = tk.StringVar()
        self.tile_width_var = tk.StringVar(value="6")
        self.tile_height_var = tk.StringVar(value="6")

            #options
        self.sandblast_var = tk.BooleanVar(value=True)
        self.localjob_var = tk.BooleanVar(value=True)
        self.full_replumb_var = tk.BooleanVar(value=False)
        self.part_replumb_var = tk.BooleanVar(value=False)
        self.min_replumb_var = tk.BooleanVar(value=False)
        self.diving_pool_var = tk.BooleanVar(value=False)

            #equipment
        self.equipment_var = tk.StringVar()
        self.quantity_var = tk.StringVar(value="1")
        self.price_var = tk.StringVar()

        self.selected_equipment = []
        self.equipment_prices = get_equipment_list()


    # ========================================================
    # GUI Layout
    # ========================================================

    def create_widgets(self):

        # ====================================================
        # Measurements
        # ====================================================
        measurements_frame = ttk.LabelFrame(
            self,
            text="Measurements",
            padding=15
        )
        measurements_frame.pack(
            fill="x",
            padx=15,
            pady=10
        )

        # ----------------------------------------------------
        # Linear Feet
        # ----------------------------------------------------

        ttk.Label(
            measurements_frame,
            text="Linear Feet(Demo):"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        ttk.Entry(
            measurements_frame,
            textvariable=self.linfeet_var,
            width=15
        ).grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )


        # ----------------------------------------------------
        # Tile Square Feet
        # ----------------------------------------------------

        ttk.Label(
            measurements_frame,
            text="Tile Square Footage:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )
        ttk.Entry(
            measurements_frame,
            textvariable=self.tile_sqft_var,
            width=15
        ).grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )
        #tile size
        ttk.Label(
            measurements_frame,
            text="Tile Width:"
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )
        ttk.Entry(
            measurements_frame,
            textvariable=self.tile_width_var,
            width=15
        ).grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )
        ttk.Label(
            measurements_frame,
            text="Tile Height:"
        ).grid(
            row=1,
            column=4,
            sticky="w",
            padx=5,
            pady=5
        )
        ttk.Entry(
            measurements_frame,
            textvariable=self.tile_height_var,
            width=15
        ).grid(
            row=1,
            column=5,
            padx=5,
            pady=5
        )
            #plaster square feet
        ttk.Label(
            measurements_frame,
            text="Plaster Square Footage:"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )
        ttk.Entry(
            measurements_frame,
            textvariable=self.plaster_sqft_var,
            width=15
        ).grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )


        # ====================================================
        # Remodel Options
        # ====================================================
        options_frame = ttk.LabelFrame(
            self,
            text="Remodel Options",
            padding=15
        )
        options_frame.pack(
            fill="x",
            padx=15,
            pady=10
        )
        #Full Replumb
        ttk.Checkbutton(
            options_frame,
            text="Full Replumb",
            variable=self.full_replumb_var
        ).grid(
            row=0,
            column=1,
            sticky="w",
            padx=10,
            pady=5
        )
        # partial replumb
        ttk.Checkbutton(
            options_frame,
            text="Partial Replumb",
            variable=self.part_replumb_var
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=10,
            pady=5
        )
        # min replumb
        ttk.Checkbutton(
            options_frame,
            text="Minimal Replumb",
            variable=self.min_replumb_var
        ).grid(
            row=0,
            column=3,
            sticky="w",
            padx=10,
            pady=5
        )
        # ----------------------------------------------------
        # Sandblast
        # ----------------------------------------------------
        ttk.Checkbutton(
            options_frame,
            text="Sandblast",
            variable=self.sandblast_var
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=5
        )

        # ----------------------------------------------------
        # Local Job
        # ----------------------------------------------------
        ttk.Checkbutton(
            options_frame,
            text="Local Job",
            variable=self.localjob_var
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=10,
            pady=5
        )
        #diving pool
        ttk.Checkbutton(
            options_frame,
            text="Diving Pool",
            variable=self.diving_pool_var
        ).grid(
            row=1,
            column=1,
            sticky="w",
            padx=10,
            pady=5
        )

        # ====================================================
        # Equipment
        # ====================================================
        equipment_frame = ttk.LabelFrame(
            self,
            text="Equipment",
            padding=15
        )
        equipment_frame.pack(
            fill="x",
            padx=15,
            pady=10
        )
        # Allow the equipment list to expand horizontally
        equipment_frame.columnconfigure(
            1,
            weight=1
        )
        # ----------------------------------------------------
        # Equipment Dropdown
        # ----------------------------------------------------
        ttk.Label(
            equipment_frame,
            text="Equipment:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )
        self.equipment_dropdown = ttk.Combobox(
            equipment_frame,
            textvariable=self.equipment_var,
            state="readonly",
            width=40,
            values=list(self.equipment_prices.keys())
        )
        self.equipment_dropdown.grid(
            row=0,
            column=1,
            sticky="w",
            padx=5,
            pady=5
        )
        # When equipment is selected, automatically load price
        self.equipment_dropdown.bind(
            "<<ComboboxSelected>>",
            self.equipment_selected
        )
        # ----------------------------------------------------
        # Quantity
        # ----------------------------------------------------
        ttk.Label(
            equipment_frame,
            text="Quantity:"
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=(15, 5),
            pady=5
        )
        ttk.Entry(
            equipment_frame,
            textvariable=self.quantity_var,
            width=8
        ).grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )
        # ----------------------------------------------------
        # Price
        # ----------------------------------------------------
        ttk.Label(
            equipment_frame,
            text="Unit Price:"
        ).grid(
            row=0,
            column=4,
            sticky="w",
            padx=(15, 5),
            pady=5
        )
        ttk.Entry(
            equipment_frame,
            textvariable=self.price_var,
            width=12
        ).grid(
            row=0,
            column=5,
            padx=5,
            pady=5
        )
        # ----------------------------------------------------
        # Add Equipment Button
        # ----------------------------------------------------
        ttk.Button(
            equipment_frame,
            text="Add Equipment",
            command=self.add_equipment
        ).grid(
            row=0,
            column=6,
            padx=(10, 5),
            pady=5
        )
        # ====================================================
        # Selected Equipment List
        # ====================================================
        equipment_list_frame = ttk.Frame(
            equipment_frame
        )
        equipment_list_frame.grid(
            row=1,
            column=0,
            columnspan=7,
            sticky="nsew",
            padx=5,
            pady=10
        )
        equipment_list_frame.columnconfigure(
            0,
            weight=1
        )
        equipment_list_frame.rowconfigure(
            0,
            weight=1
        )

        # ----------------------------------------------------
        # Treeview
        # ----------------------------------------------------
        self.equipment_tree = ttk.Treeview(
            equipment_list_frame,
            columns=(
                "equipment",
                "quantity",
                "price",
                "total"
            ),
            show="headings",
            height=6
        )
        self.equipment_tree.heading(
            "equipment",
            text="Equipment"
        )
        self.equipment_tree.heading(
            "quantity",
            text="Quantity"
        )
        self.equipment_tree.heading(
            "price",
            text="Unit Price"
        )
        self.equipment_tree.heading(
            "total",
            text="Total"
        )

        # ----------------------------------------------------
        # Treeview Column Sizes
        # ----------------------------------------------------
        self.equipment_tree.column(
            "equipment",
            width=250,
            anchor="w"
        )
        self.equipment_tree.column(
            "quantity",
            width=100,
            anchor="center"
        )
        self.equipment_tree.column(
            "price",
            width=120,
            anchor="e"
        )
        self.equipment_tree.column(
            "total",
            width=130,
            anchor="e"
        )
        self.equipment_tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # ----------------------------------------------------
        # Scrollbar
        # ----------------------------------------------------
        equipment_scrollbar = ttk.Scrollbar(
            equipment_list_frame,
            orient="vertical",
            command=self.equipment_tree.yview
        )
        equipment_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )
        self.equipment_tree.configure(
            yscrollcommand=equipment_scrollbar.set
        )
        # Double-click equipment to edit it
        self.equipment_tree.bind(
            "<Double-1>",
            lambda event: self.edit_equipment()
        )

        # ====================================================
        # Equipment Buttons
        # ====================================================
        equipment_buttons_frame = ttk.Frame(
            equipment_frame
        )
        equipment_buttons_frame.grid(
            row=2,
            column=0,
            columnspan=7,
            pady=5
        )
        ttk.Button(
            equipment_buttons_frame,
            text="Edit Selected",
            command=self.edit_equipment
        ).pack(
            side="left",
            padx=5
        )
        ttk.Button(
            equipment_buttons_frame,
            text="Remove Selected",
            command=self.remove_equipment
        ).pack(
            side="left",
            padx=5
        )


        # ----------------------------------------------------
        # Equipment Total
        # ----------------------------------------------------
        self.equipment_total_label = ttk.Label(
            equipment_frame,
            text="Equipment Total: $0.00",
            font=("TkDefaultFont", 10, "bold")
        )

        self.equipment_total_label.grid(
            row=3,
            column=0,
            columnspan=7,
            sticky="e",
            padx=5,
            pady=(5, 0)
        )

        # ====================================================
        # Calculate Button
        # ====================================================

        ttk.Button(
            self,
            text="Calculate Estimate",
            command=self.calculate
        ).pack(
            pady=15
        )

        # ====================================================
        # Results Window
        # ====================================================

        results_frame = ttk.LabelFrame(
            self,
            text="Estimate",
            padding=15
        )
        results_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )
        self.results_text = tk.Text(
            results_frame,
            height=12,
            width=70,
            state="disabled"
        )
        self.results_text.pack(
            fill="both",
            expand=True
        )


    # ========================================================
    # Equipment Selected From Dropdown
    # ========================================================
    def equipment_selected(self, event=None):
        equipment = self.equipment_var.get()
        if equipment in self.equipment_prices:
            price = self.equipment_prices[equipment]
            self.price_var.set(
                f"{price:.2f}"
            )

    # ========================================================
    # Add Equipment
    # ========================================================
    def add_equipment(self):
        equipment = self.equipment_var.get()
        if not equipment:
            messagebox.showerror(
                "No Equipment",
                "Please select a piece of equipment."
            )
            return

        try:
            quantity = int(
                self.quantity_var.get()
            )
            if quantity <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Invalid Quantity",
                "Quantity must be a positive whole number."
            )
            return

        try:
            price = float(self.price_var.get())
            if price < 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Invalid Price",
                "Price must be a valid number."
            )
            return

        for item in self.selected_equipment:
            if item["name"] == equipment:
                item["quantity"] += quantity
                item["price"] = price
                self.refresh_equipment_list()
                self.clear_equipment_inputs()
                return

        self.selected_equipment.append({
            "name": equipment,
            "quantity": quantity,
            "price": price
        })

        self.refresh_equipment_list()
        self.clear_equipment_inputs()


    def clear_equipment_inputs(self):
        self.equipment_var.set("")
        self.quantity_var.set("1")
        self.price_var.set("")


    def refresh_equipment_list(self):
        for item in self.equipment_tree.get_children():
            self.equipment_tree.delete(item)
        for equipment in self.selected_equipment:
            line_total = (
                equipment["quantity"]
                * equipment["price"]
            )
            self.equipment_tree.insert(
                "",
                "end",
                values=(
                    equipment["name"],
                    equipment["quantity"],
                    f"${equipment['price']:,.2f}",
                    f"${line_total:,.2f}"
                )
            )

        equipment_total = self.get_equipment_total()
        self.equipment_total_label.config(
            text=f"Equipment Total: ${equipment_total:,.2f}"
        )


    def get_equipment_total(self):
        total = 0.0
        for equipment in self.selected_equipment:
            total += (
                equipment["quantity"]
                * equipment["price"]
            )
        return total


    def edit_equipment(self):
        selected = self.equipment_tree.selection()
        if not selected:
            messagebox.showerror(
                "No Selection",
                "Please select equipment to edit."
            )
            return

        selected_index = self.equipment_tree.index(selected[0])
        equipment = self.selected_equipment[selected_index]
        edit_window = tk.Toplevel(self)
        edit_window.title("Edit Equipment")
        edit_window.geometry("350x220")
        edit_window.resizable(False,False)
        edit_window.transient(self)
        edit_window.grab_set()

        ttk.Label(
            edit_window,
            text="Equipment:"
        ).pack(
            pady=(15, 5)
        )
        ttk.Label(
            edit_window,
            text=equipment["name"],
            font=("TkDefaultFont", 10, "bold")
        ).pack(
            pady=5
        )

        ttk.Label(
            edit_window,
            text="Quantity:"
        ).pack(
            pady=(5, 2)
        )
        quantity_var = tk.StringVar(
            value=str(
                equipment["quantity"]
            )
        )
        quantity_entry = ttk.Entry(
            edit_window,
            textvariable=quantity_var,
            width=15
        )
        quantity_entry.pack(
            pady=2
        )

        ttk.Label(
            edit_window,
            text="Unit Price:"
        ).pack(
            pady=(5, 2)
        )
        price_var = tk.StringVar(
            value=f"{equipment['price']:.2f}"
        )
        price_entry = ttk.Entry(
            edit_window,
            textvariable=price_var,
            width=15
        )
        price_entry.pack(
            pady=2
        )


        def save_changes():
            # Validate quantity
            try:
                new_quantity = int(quantity_var.get())
                if new_quantity <= 0:
                    raise ValueError

            except ValueError:
                messagebox.showerror(
                    "Invalid Quantity",
                    "Quantity must be a positive whole number.",
                    parent=edit_window
                )
                return

            # Validate price
            try:
                new_price = float(price_var.get())
                if new_price < 0:
                    raise ValueError

            except ValueError:
                messagebox.showerror(
                    "Invalid Price",
                    "Price must be a valid number.",
                    parent=edit_window
                )
                return


            # Update dictionary
            equipment["quantity"] = new_quantity
            equipment["price"] = new_price

            # Refresh GUI
            self.refresh_equipment_list()

            # Close window
            edit_window.destroy()


        ttk.Button(
            edit_window,
            text="Save Changes",
            command=save_changes
        ).pack(
            pady=12
        )

        quantity_entry.focus()


    def remove_equipment(self):
        selected = self.equipment_tree.selection()
        if not selected:
            messagebox.showerror(
                "No Selection",
                "Please select equipment to remove."
            )
            return

        selected_index = self.equipment_tree.index(selected[0])
        del self.selected_equipment[selected_index]
        self.refresh_equipment_list()


    def calculate(self):
        # sending all the user selections to the calculator
        try:
            measurements = {
                "prep_linear_feet":float(self.linfeet_var.get()),
                "tile_sqft":float( self.tile_sqft_var.get()),
                "plaster_sqft":float(self.plaster_sqft_var.get()),
                "tile_width":float(self.tile_width_var.get()),
                "tile_height":float(self.tile_height_var.get()),
            }

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numbers for all measurements."
            )
            return

        options = {
            "sandblast":self.sandblast_var.get(),
            "localjob":self.localjob_var.get(),
            "fullplumb":self.full_replumb_var.get(),
            "partplumb":self.part_replumb_var.get(),
            "minplumb":self.min_replumb_var.get(),
            "divepool":self.diving_pool_var.get(),
        }

        equipment = self.selected_equipment

        result = calculate_estimate(
            measurements,
            options,
            equipment
        )


        #show results in box

        output = f"""
REMODEL ESTIMATE
==============================
Prep:           {result["prep_total"]:>14,.2f}
Tile:           {result["tile_total"]:>14,.2f}
Equipment:      {result["equipment_total"]:>14,.2f}
Plumbing:       {result["plumbing_total"]:>14,.2f}
Plaster:        {result["plaster_total"]:>14,.2f}

Total:          {result["total_cost"]:>14,.2f}
==============================
"""


        self.results_text.config(state="normal")
        self.results_text.delete("1.0",tk.END)
        self.results_text.insert( "1.0",output)
        self.results_text.config(state="disabled")




# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    app = RemodelEstimator()
    app.mainloop()