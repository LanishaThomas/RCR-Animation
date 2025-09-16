from manim import *

class RCRIntro(Scene):
    def construct(self):
        points = [
            ("One-byte or two-byte instruction depending on how you write it:\n"
             "RCR reg, 1 → 1 byte (opcode + register code).\n"
             "RCR reg, CL or RCR reg, imm → 2–3 bytes (opcode + modR/M + immediate).", BLUE),

            ("Operands: Register or Memory, rotation count can be 1, CL, or immediate", GREEN),

            ("Operation: Bits shifted right → LSB enters CF, old CF enters MSB", ORANGE),

            ("Flags Affected: CF, OF", RED),

            ("Difference from ROR: RCR rotates through carry; ROR rotates only operand bits", PURPLE),

            ("Applications: Multi-precision arithmetic, shifting large numbers with carry", TEAL),
        ]

        # Title at top
        title = Text("RCR Instruction", font_size=40, color=YELLOW).to_edge(UP)

        # Create text objects for points
        text_objects = [Text(txt, color=color, font_size=28) for txt, color in points]

        # Arrange vertically below the title
        bullet_points = VGroup(*text_objects).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        bullet_points.next_to(title, DOWN, buff=0.8).to_edge(LEFT)

        # Animate title first
        self.play(Write(title))
        self.wait(0.5)

        # Animate bullet points one by one
        for t in bullet_points:
            self.play(Write(t))
            self.wait(0.5)

        self.wait(2)

class MicroProgramIntro(Scene):
    def construct(self):
        # Big heading in center (default position is center)
        heading = Text(
            "Now let's see the microprogram for \nRCR R1, 02H",
            font_size=40,
            color=YELLOW
        ).scale(1.1)

        # Animate appearance
        self.play(Write(heading), run_time=2)
        self.wait(2)


class ArchitectureDiagram(Scene):
    def construct(self):
        # Internal Processor Bus (vertical line in center)
        
        bus = Line(UP*4, DOWN*4, color=WHITE).shift(RIGHT*0)

        # ===== Left side blocks =====
        pc = Rectangle(width=1.2, height=0.5, color=BLUE).shift(LEFT*4+UP*3)
        pc_label = Text("PC", font_size=20).move_to(pc.get_center())

        mar = Rectangle(width=1.2, height=0.5, color=BLUE).shift(LEFT*4+UP*2)
        mar_label = Text("MAR", font_size=20).move_to(mar.get_center())

        mdr = Rectangle(width=1.2, height=0.5, color=BLUE).shift(LEFT*4+UP*1)
        mdr_label = Text("MDR", font_size=20).move_to(mdr.get_center())

        memory = Rectangle(width=1.5, height=0.8, color=GREEN).shift(LEFT*6+UP*1.5)
        memory_label = Text("Memory", font_size=18).move_to(memory.get_center())

        ir = Rectangle(width=1.2, height=0.5, color=BLUE).shift(RIGHT*4+UP*1.5)
        ir_label = Text("IR", font_size=20).move_to(ir.get_center())

        # ===== Right side blocks =====
        r0 = Rectangle(width=1.2, height=0.5, color=BLUE).shift(RIGHT*4+UP*0.5)
        r0_label = Text("R0", font_size=20).move_to(r0.get_center())

        r1 = Rectangle(width=1.2, height=0.5, color=BLUE).shift(RIGHT*4+DOWN*0.2)
        r1_label = Text("R1", font_size=20).move_to(r1.get_center())

        rn = Rectangle(width=1.2, height=0.5, color=BLUE).shift(RIGHT*4+DOWN*2)
        rn_label = Text("R(n-1)", font_size=20).move_to(rn.get_center())

        y_reg = Rectangle(width=1.2, height=0.5, color=BLUE).shift(LEFT*2+DOWN*0)
        y_label = Text("Y", font_size=20).move_to(y_reg.get_center())

        select_4 = Rectangle(width=1.2, height=0.5, color=BLUE).shift(LEFT*4+DOWN*0)
        select_4_label = Text("Select 4", font_size=20).move_to(select_4.get_center())

        mux = Rectangle(width=1.2, height=0.5, color=ORANGE).shift(LEFT*3+DOWN*1)
        mux_label = Text("MUX", font_size=20).move_to(mux.get_center())

        alu = Rectangle(width=1.6, height=1, color=YELLOW).shift(LEFT*3+DOWN*2.3)
        alu_label = Text("ALU", font_size=20).move_to(alu.get_center())

        z_reg = Rectangle(width=1.2, height=0.5, color=BLUE).shift(LEFT*3+DOWN*3.4)
        z_label = Text("Z", font_size=20).move_to(z_reg.get_center())

        temp = Rectangle(width=1.2, height=0.5, color=BLUE).shift(RIGHT*4+DOWN*3)
        temp_label = Text("Temp", font_size=20).move_to(temp.get_center())

        # ===== Control Unit =====
        cu = Rectangle(width=2.5, height=1, color=PURPLE).shift(RIGHT*4+UP*3)
        cu_label = Text("Instruction Decoding\n& Control Unit", font_size=16).move_to(cu.get_center())

        # ===== Arrows =====

        # Double-sided arrows to internal bus
        pc_to_bus = DoubleArrow(start=pc.get_right(), end=bus.get_left()+UP*3, buff=0.1, color=WHITE)
        mdr_to_bus = DoubleArrow(start=mdr.get_right(), end=bus.get_left()+UP*1, buff=0.1, color=WHITE)
        r0_to_bus = DoubleArrow(start=r0.get_left(), end=bus.get_left()+UP*0.5, buff=0.1, color=WHITE)
        r1_to_bus = DoubleArrow(start=r1.get_left(), end=bus.get_left()+DOWN*0.2, buff=0.1, color=WHITE)
        rn_to_bus = DoubleArrow(start=rn.get_left(), end=bus.get_left()+DOWN*2, buff=0.1, color=WHITE)
        temp_to_bus = DoubleArrow(start=temp.get_left(), end=bus.get_right()+DOWN*3, buff=0.1, color=WHITE)
        mdr_to_memory = DoubleArrow(start=mdr.get_left(), end=memory.get_right(), buff=0.1, color=WHITE)

        # Single arrows
        bus_to_mar = Arrow(start=bus.get_right()+UP*2, end=mar.get_right(), buff=0.1, color=WHITE)
        ir_to_cu = Arrow(start=ir.get_top(), end=cu.get_bottom(), buff=0.1, color=WHITE)
        bus_to_ir = Arrow(start=bus.get_right()+UP*1.5, end=ir.get_left(), buff=0.1, color=WHITE)  # Ensure IR aligns with bus
        bus_to_y = Arrow(start=bus.get_right()+DOWN*0, end=y_reg.get_right(), buff=0.1, color=WHITE)
        bus_to_alu = Arrow(start=bus.get_right()+DOWN*2.3, end=alu.get_right(), buff=0.1, color=WHITE)
        mar_to_memory = Arrow(start=mar.get_left(), end=memory.get_right(), buff=0.1, color=WHITE)
        cu_to_bus = Arrow(start=cu.get_left(), end=bus.get_right()+UP*3, buff=0.1, color=WHITE)
        y_to_mux = Arrow(start=y_reg.get_bottom(), end=mux.get_top(), buff=0.1, color=WHITE)
        select_4_to_mux = Arrow(start=select_4.get_bottom(), end=mux.get_top(), buff=0.1, color=WHITE)
        mux_to_alu = Arrow(start=mux.get_bottom(), end=alu.get_top(), buff=0.1, color=WHITE)
        alu_to_z = Arrow(start=alu.get_bottom(), end=z_reg.get_top(), buff=0.1, color=WHITE)
        z_to_bus = Arrow(start=z_reg.get_right(), end=bus.get_left()+DOWN*3.4, buff=0.1, color=WHITE)

        select_label = Text("Select", font_size=15).shift(LEFT*5+DOWN*1)
        select_arrow = Arrow(start=select_label.get_right(), end=mux.get_left(), buff=0.1, color=WHITE)

        select_function_label = Text("Select Function", font_size=15).shift(LEFT*5+DOWN*2.3)
        select_function_arrow = Arrow(start=select_function_label.get_right(), end=alu.get_left(), buff=0.1, color=WHITE)

        carry_label = Text("Carry-in", font_size=15).shift(LEFT*1+DOWN*2.7)
        carry_arrow = Arrow(end=alu.get_right()+DOWN*0.3, start=carry_label.get_left(), buff=0.1, color=WHITE)

        bus_label = Text("Internal Processor Bus", font_size=20, color=YELLOW).shift(LEFT*0+UP*3.7)

        vertical_dots = VGroup()
        for i in range(3):
            dot = Circle(radius=0.05, color=WHITE, fill_opacity=1)
            vertical_dots.add(dot)

        vertical_dots.arrange(DOWN, buff=0.2)  # Arrange the dots vertically
        vertical_dots.move_to(RIGHT*4+DOWN*1.1)  # Position them between R1 and Rn

        self.play(Create(bus))
        self.play(Create(pc), Write(pc_label),
                  Create(mar), Write(mar_label),
                  Create(mdr), Write(mdr_label),
                  Create(memory), Write(memory_label),
                  Create(ir), Write(ir_label),
                  Create(r0), Write(r0_label),
                  Create(r1), Write(r1_label),
                  Create(rn), Write(rn_label),
                  Create(y_reg), Write(y_label),
                  Create(mux), Write(mux_label),
                  Create(select_4), Write(select_4_label),
                  Create(alu), Write(alu_label),
                  Create(z_reg), Write(z_label),
                  Create(temp), Write(temp_label),
                  Create(cu), Write(cu_label),
                  Create(vertical_dots))

        # Animate arrows
        self.play(Create(pc_to_bus), Create(mdr_to_bus), Create(r0_to_bus),
                  Create(r1_to_bus),Create(ir_to_cu), Create(rn_to_bus), Create(temp_to_bus),
                  Create(mdr_to_memory), Create(bus_to_mar), Create(bus_to_ir),
                  Create(bus_to_y), Create(bus_to_alu), Create(mar_to_memory),
                  Create(cu_to_bus), Create(y_to_mux), Create(select_4_to_mux),
                  Create(mux_to_alu),Create(z_to_bus), Create(alu_to_z),Create(carry_label),Create(carry_arrow),
                  Create(select_label), Create(select_arrow), Create(select_function_label), 
                  Create(select_function_arrow),Create(bus_label),)
        
                  # === Caption (T1) ===
        caption = Text("T1: PCout, MARin, Read, Select 4, Add, Zin", 
                       font_size=22, color=YELLOW).to_edge(DR).shift(DOWN*0.5)
        self.play(FadeIn(caption))

        # --- Step 1: PCout -> MARin ---
        signal_red = Dot(color=RED, radius=0.08)  # RED dot will persist
        path_pc_to_bus = Line(pc.get_right(), [bus.get_x(), pc.get_y(), 0])
        self.play(MoveAlongPath(signal_red, path_pc_to_bus), run_time=1.5)
        path_bus_down = Line([bus.get_x(), pc.get_y(), 0], [bus.get_x(), mar.get_y(), 0])
        self.play(MoveAlongPath(signal_red, path_bus_down), run_time=1.5)
        path_bus_to_mar = Line([bus.get_x(), mar.get_y(), 0], mar.get_right())
        self.play(MoveAlongPath(signal_red, path_bus_to_mar), run_time=1.5)
        self.play(Indicate(mar))

        # --- Step 2: MAR -> Memory (Read) ---
        path2 = Line(mar.get_left(), memory.get_right())
        self.play(MoveAlongPath(signal_red, path2), run_time=1.5)
        read_text = Text("Read", font_size=18, color=YELLOW).next_to(memory, UP)
        self.play(Write(read_text))
        self.wait(0.8)
        self.play(Indicate(memory))

        # --- Step 3: Select4 -> ALU (Yellow dot) ---
        signal_yellow = Dot(color=YELLOW, radius=0.08).move_to(select_4.get_bottom())
        self.play(FadeIn(signal_yellow))
        self.play(Indicate(select_4))
        path4a = Line(select_4.get_bottom(), mux.get_top())
        self.play(MoveAlongPath(signal_yellow, path4a), run_time=1.0)
        path4b = Line(mux.get_bottom(), alu.get_top())
        self.play(MoveAlongPath(signal_yellow, path4b), run_time=1.5)
        self.play(Indicate(alu))
        self.play(FadeOut(signal_yellow))
               # --- Step 4: Bus -> ALU (Red dot enters ALU from bus) ---
        signal_from_bus = Dot(color=RED, radius=0.08).move_to([bus.get_x(), alu.get_y(), 0])
        self.play(FadeIn(signal_from_bus))

        path_bus_to_alu = Line([bus.get_x(), alu.get_y(), 0], alu.get_right())
        self.play(MoveAlongPath(signal_from_bus, path_bus_to_alu), run_time=1.5)

        self.play(Indicate(alu))
        self.play(FadeOut(signal_from_bus))   # 🔴 disappears inside ALU

        # ALU "Add" text
        add_text = Text("Add", font_size=18, color=YELLOW).next_to(select_function_label, DOWN).shift(RIGHT*0.5)
        self.play(Write(add_text))
        self.wait(1)
        self.play(FadeOut(add_text))

        # --- Step 5: ALU -> Z (Orange dot) ---
        signal_orange = Dot(color=ORANGE, radius=0.08).move_to(alu.get_bottom())
        self.play(FadeIn(signal_orange))

        path_alu_to_z = Line(alu.get_bottom(), z_reg.get_top())
        self.play(MoveAlongPath(signal_orange, path_alu_to_z), run_time=1.5)

        self.play(Indicate(z_reg))
        self.play(FadeOut(signal_orange))

                # === T2 (as before, keep WMFC blink) ===
        new_caption = Text("T2: Zout, PCin, Yin, WMFC", font_size=22, color=YELLOW).to_edge(DR).shift(DOWN*0.5)
        self.play(Transform(caption, new_caption))

        # Z -> bus (horizontal move)
        path_z_to_bus = Line(z_reg.get_right(), [bus.get_x(), z_reg.get_y(), 0])
        self.play(MoveAlongPath(signal_orange, path_z_to_bus), run_time=1.2)

        # bus moves vertically up/down to PC's level
        path_bus_up_to_pc = Line([bus.get_x(), z_reg.get_y(), 0], [bus.get_x(), pc.get_y(), 0])
        self.play(MoveAlongPath(signal_orange, path_bus_up_to_pc), run_time=1.2)

        # bus -> PC (horizontal move)
        path_bus_to_pc = Line([bus.get_x(), pc.get_y(), 0], pc.get_left())
        self.play(MoveAlongPath(signal_orange, path_bus_to_pc), run_time=1.5)
  


        self.play(Indicate(pc))
        self.play(FadeOut(signal_orange))   # 🟠 will disappear correctly now

              # PC -> Y (horizontal move)
        path_bus_to_y = Line([bus.get_x(), y_reg.get_y(), 0], y_reg.get_left())
        self.play(MoveAlongPath(signal_orange, path_bus_to_y), run_time=1.5)

        # Highlight and finish
        self.play(Indicate(y_reg))
        self.play(FadeOut(signal_orange))  # 🟠 will disappear correctly now





        # (use same flow as before for T2)...

        # === Update Caption to T3 ===
        new_caption_t3 = Text("T3: MDRout, IRin", font_size=22, color=YELLOW).to_edge(DR).shift(DOWN*0.5)
        self.play(Transform(caption, new_caption_t3))

        # --- Step (T3): Memory -> MDR -> IR ---
        # Red dot waiting at Memory moves again
        wmfc_text = Text("MFC", font_size=18, color=YELLOW).next_to(memory, DOWN).shift(RIGHT*0.5)
        self.play(Write(wmfc_text))
        for _ in range(2):
            self.play(memory.animate.set_fill(GREEN, opacity=0.5), run_time=0.3)
            self.play(memory.animate.set_fill(opacity=0), run_time=0.3)
        self.play(FadeOut(read_text))
        self.play(FadeOut(wmfc_text))
        path_mem_to_mdr = Line(memory.get_right(), mdr.get_left())
        self.play(MoveAlongPath(signal_red, path_mem_to_mdr), run_time=1.5)
        self.play(Indicate(mdr))
        path_mdr_to_bus = Line(mdr.get_right(), [bus.get_x(), mdr.get_y(), 0])
        self.play(MoveAlongPath(signal_red, path_mdr_to_bus), run_time=1.5)
        path_bus_to_ir = Line([bus.get_x(), ir.get_y(), 0], ir.get_left())
        self.play(MoveAlongPath(signal_red, path_bus_to_ir), run_time=1.5)
        # Correct path from IR to CU
        # IR -> CU (top of IR to bottom of CU)
        path_ir_to_cu = Line(ir.get_top(), cu.get_bottom())
        self.play(MoveAlongPath(signal_red, path_ir_to_cu), run_time=1.5)
        self.play(Indicate(cu))



        self.wait(1)
        self.play(FadeOut(signal_red))  # Red dot disappears at IR

                # === Update Caption to T4 ===
        new_caption_t4 = Text("T4: Immediate field of IRout, Yin", 
                              font_size=22, color=YELLOW).to_edge(DR).shift(DOWN*0.5)
        self.play(Transform(caption, new_caption_t4))

        # --- Step (T4): IR -> Bus -> Select Y (Pink dot) ---
        signal_pink = Dot(color=PINK, radius=0.08).move_to(ir.get_left())
        self.play(FadeIn(signal_pink))

        # IR -> Bus (horizontal)
        path_ir_to_bus = Line(ir.get_left(), [bus.get_x(), ir.get_y(), 0])
        self.play(MoveAlongPath(signal_pink, path_ir_to_bus), run_time=1.2)

        # Bus travels vertically to Select Y’s level
        path_bus_to_y = Line([bus.get_x(), ir.get_y(), 0], [bus.get_x(), y_reg.get_y(), 0])
        self.play(MoveAlongPath(signal_pink, path_bus_to_y), run_time=1.2)

        # Bus -> Right side of Select Y
        path_bus_to_select_y = Line([bus.get_x(), y_reg.get_y(), 0], y_reg.get_right())
        self.play(MoveAlongPath(signal_pink, path_bus_to_select_y), run_time=1.5)

        self.play(Indicate(y_reg))
           # Dot disappears at Select Y


        # === Update Caption to T4 ===
        new_caption_t4 = Text("T5: R1out, Select Y,\n Rotate Right with Carry, Zin", 
                              font_size=22, color=YELLOW).to_edge(DR).shift(DOWN*0.5)
        self.play(Transform(caption, new_caption_t4))

        signal_green = Dot(color=GREEN, radius=0.08).move_to(alu.get_right())
        self.play(FadeIn(signal_green))

        # --- T4: R1 -> ALU (via bus, skipping Yin) ---

        # R1 -> bus (horizontal move)
        path_ir_to_bus = Line(r1.get_right(), [bus.get_x(), r1.get_y(), 0])
        self.play(MoveAlongPath(signal_green, path_ir_to_bus), run_time=1.2)

        # bus -> down/up to ALU's level
        path_bus_to_alu_y = Line([bus.get_x(), r1.get_y(), 0], [bus.get_x(), alu.get_y(), 0])
        self.play(MoveAlongPath(signal_green, path_bus_to_alu_y), run_time=1.2)

        # bus -> ALU (horizontal move)
        path_bus_to_alu = Line([bus.get_x(), alu.get_y(), 0], alu.get_right())
        self.play(MoveAlongPath(signal_green, path_bus_to_alu), run_time=1.5)

        self.play(Indicate(alu))
        self.play(FadeOut(signal_pink))

        signal_yellow = Dot(color=PINK, radius=0.08).move_to(y_reg.get_bottom())
        self.play(FadeIn(signal_yellow))
        path4a = Line(y_reg.get_bottom(), mux.get_top())
        self.play(MoveAlongPath(signal_yellow, path4a), run_time=1.0)
        path4b = Line(mux.get_bottom(), alu.get_top())
        self.play(MoveAlongPath(signal_yellow, path4b), run_time=1.5)
        
               # --- Step 4: Bus -> ALU (Red dot enters ALU from bus) ---
        
        self.play(Indicate(alu))
        self.play(FadeOut(signal_yellow))
        

        
               # --- Step 4: Bus -> ALU (Red dot enters ALU from bus) ---
        

        self.play(FadeOut(signal_green))   # 🔴 disappears inside ALU

        # Blink ALU (Rotate Right with Carry)
        rcr_text = Text("RCR", font_size=18, color=YELLOW).next_to(select_function_label, DOWN).shift(RIGHT*0.5)
        self.play(Write(rcr_text))
        for _ in range(2):
            self.play(alu.animate.set_fill(GREEN, opacity=0.5), run_time=0.3)
            self.play(alu.animate.set_fill(opacity=0), run_time=0.3)
        signal_pink = Dot(color=PINK, radius=0.08).move_to(z_reg.get_right())
        self.play(FadeIn(signal_pink))
        self.play(FadeOut(rcr_text))

        path_alu_to_z = Line(alu.get_bottom(), z_reg.get_top())
        self.play(MoveAlongPath(signal_pink, path_alu_to_z), run_time=1.5)

        # === Update Caption to T5 ===
        new_caption_t5 = Text("T6: Zout, R1in, End", font_size=22, color=YELLOW).to_edge(DR).shift(DOWN*0.5)
        self.play(Transform(caption, new_caption_t5))

        # --- Step (T5): Zout -> R1in ---
        self.play(Indicate(z_reg))
        

        path_z_to_bus2 = Line(z_reg.get_top(), [bus.get_x(), z_reg.get_y(), 0])
        self.play(MoveAlongPath(signal_pink, path_z_to_bus2), run_time=1.2)

        path_bus_up_to_r1 = Line([bus.get_x(), z_reg.get_y(), 0], [bus.get_x(), r1.get_y(), 0])
        self.play(MoveAlongPath(signal_pink, path_bus_up_to_r1), run_time=1.2)

        path_bus_to_r1 = Line([bus.get_x(), r1.get_y(), 0], r1.get_left())
        self.play(MoveAlongPath(signal_pink, path_bus_to_r1), run_time=1.5)
        end_text = Text("END", font_size=18, color=YELLOW).next_to(r1, DOWN).shift(RIGHT*0.5)
        self.play(Write(end_text))

        self.play(Indicate(r1))
        self.play(FadeOut(signal_pink)) 
        self.play(FadeOut(end_text))   # 🟢 disappears at R1


class RCRVisualization(Scene):
    def construct(self):
        # --- Title ---
        title = Text("RCR Working", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # --- Initial R1 value ---
        r1_value_text = Text("R1 = 11001010", font_size=28, color=WHITE).next_to(title, DOWN, buff=0.6)
        self.play(Write(r1_value_text))

        instr_text = Text("RCR R1, 02H", font_size=28, color=BLUE).next_to(r1_value_text, DOWN, buff=0.5)
        self.play(Write(instr_text))

        # --- Create bit boxes D7..D0 ---
        bits = list("11001010")  # R1 value
        boxes = VGroup()
        bit_labels = []

        for i, bit in enumerate(bits):
            box = Square(0.7).shift(RIGHT * (i - 3.5))  # center align
            boxes.add(box)
            label = Text(bit, font_size=24).move_to(box.get_center())
            bit_labels.append(label)

        boxes.next_to(instr_text, DOWN, buff=1.0)
        self.play(Create(boxes), *[Write(lbl) for lbl in bit_labels])

        # --- D7..D0 labels ---
        index_labels = VGroup()
        for i, box in enumerate(boxes):
            lbl = Text(f"D{7-i}", font_size=20, color=GRAY).next_to(box, DOWN, buff=0.2)
            index_labels.add(lbl)
        self.play(Write(index_labels))

        # --- Carry box BESIDE D0 ---
        carry_box = Square(0.7).next_to(boxes[-1], RIGHT, buff=1.0)
        carry_label = Text("0", font_size=24).move_to(carry_box.get_center())
        carry_name = Text("Carry", font_size=20, color=GRAY).next_to(carry_box, DOWN, buff=0.2)
        self.play(Create(carry_box), Write(carry_label), Write(carry_name))

        # --- Overflow Flag box BELOW carry label ---
        of_box = Square(0.7).next_to(carry_name, DOWN, buff=0.6)
        of_label = Text("", font_size=24).move_to(of_box.get_center())
        of_name = Text("OF", font_size=20, color=GRAY).next_to(of_box, DOWN, buff=0.2)
        self.play(Create(of_box), Write(of_label), Write(of_name))

        # --- Explanation below OF ---
        of_explanation = Text(
            "OF = MSB XOR CF \n (only valid for 1 rotation)",
            font_size=20, color=YELLOW
        ).next_to(of_box, DOWN, buff=0.5)
        self.play(Write(of_explanation))

        # --- Narration placeholder ---
        narration = Text("", font_size=22, color=YELLOW).to_edge(DOWN)
        self.add(narration)

        # 🔄 Updated helper function
        def rcr_once(step_num, update_of=True):
            nonlocal bit_labels, carry_label

            # --- Step 1: D0 -> Carry ---
            self.play(Transform(narration, Text(
                f"Rotation {step_num}: Step 1 D0 → Carry",
                font_size=22, color=YELLOW).to_edge(DOWN))
            )
            d0_label = bit_labels[-1]

            # Save old carry text before updating
            old_carry_text = carry_label.text  

            # Animate D0 moving into carry box
            self.play(d0_label.animate.move_to(carry_box.get_center()), run_time=1)
            self.remove(d0_label)

            # 🔴 Remove old carry label to avoid overwriting
            self.remove(carry_label)

            # Add the new carry label
            carry_label = Text(d0_label.text, font_size=24).move_to(carry_box.get_center())
            self.add(carry_label)

            # --- Step 2: Old Carry waits beside D7 ---
            waiting_carry = Text(old_carry_text, font_size=24).next_to(boxes[0], LEFT, buff=0.5)
            self.play(FadeIn(waiting_carry))

            # --- Step 3: Shift bits right ---
            self.play(Transform(narration, Text(
                f"Rotation {step_num}: Step 2 Bits shift right",
                font_size=22, color=YELLOW).to_edge(DOWN))
            )
            for i in reversed(range(len(bit_labels) - 1)):
                old_label = bit_labels[i]
                target_box = boxes[i + 1]
                self.play(old_label.animate.move_to(target_box.get_center()), run_time=0.6)
                self.remove(old_label)
                new_label = Text(old_label.text, font_size=24).move_to(target_box.get_center())
                bit_labels[i + 1] = new_label
                self.add(new_label)

            # --- Step 4: Waiting carry → D7 ---
            self.play(Transform(narration, Text(
                f"Rotation {step_num}: Step 3 Old Carry → D7",
                font_size=22, color=YELLOW).to_edge(DOWN))
            )
            self.play(waiting_carry.animate.move_to(boxes[0].get_center()), run_time=1)
            self.remove(waiting_carry)
            bit_labels[0] = Text(old_carry_text, font_size=24).move_to(boxes[0].get_center())
            self.add(bit_labels[0])

            # --- Step 5: Update OF ---
            if update_of:
                self.play(Transform(narration, Text(
                    "Step 4: Update OF = D7 XOR D6",
                    font_size=22, color=YELLOW).to_edge(DOWN))
                )
                msb_new = int(bit_labels[0].text)      # D7
                second_msb_new = int(bit_labels[1].text)  # D6
                of_value = msb_new ^ second_msb_new
                of_label.become(Text(str(of_value), font_size=24).move_to(of_box.get_center()))
            else:
                self.play(Transform(narration, Text(
                    "OF undefined for multi-bit rotates",
                    font_size=22, color=YELLOW).to_edge(DOWN))
                )
                of_label.become(Text("—", font_size=24, color=RED).move_to(of_box.get_center()))


        # 🔁 Perform two rotations
        rcr_once(1, update_of=True)
        rcr_once(2, update_of=False)

        # --- Final Label: Result goes to Z ---
        final_label = Text("Final Output goes to Z", font_size=28, color=GREEN).next_to(boxes, DOWN, buff=1.5)
        self.play(Write(final_label))

        self.wait(2)


class RCROutro(Scene):
    def construct(self):
        # Big "THE END" at the center
        end_text = Text("THE END", font_size=120, color=YELLOW).scale(1.2)
        self.play(Write(end_text), run_time=2)
        self.wait(1)

        # Your signature at bottom-right
        by_text = Text("BY - Lanisha Thomas", font_size=32, color=BLUE)
        by_text.to_corner(DR, buff=0.5)  # DR = Down Right
        self.play(FadeIn(by_text, shift=DOWN))
        self.wait(2)

