
<img src="https://github.com/mrk-fox/MHIPS/blob/main/pictures/MHIPS%20Zine.png" style="width:auto;">

<h1 align="center">MHIPS</h1>
<div align="center">Modular Human Interface Panels System</div>
<br> <br>
# Introduction
As controlling any type of craft with electronical components reqiring human intervention to function grows with the complexity of the craft and its tasks, I have decided to design a controlling system which is modular and uses near-aerospace-safety protocolls.


**Please pay attention to the fact that this project is still being developed. There is no "final solution" or such similar.**

## Functionality and goals

Every sucesfull project resembles a solution for a problem. Thus, the problem needs to be formulated before a solution is deigned. The problem that this project solves is the complexity of digital menus and the lack of haptic response in controlling anything with pure software.
My solution is a _modular, standartized panel system_ 
Hence, a ruleset was reqired to ensure the mulitcompatiability and extensiabiliy of this project.

# Standartization

In this section we define a convention for the MHIPS (Modular Human Interface Panel System).
``` 
1. The abbreviation "MHIPS" stands for "Modular Human Interface Panel System".
      a. A panel is defined as a mounted and rigid resembly of multiple tiles, solving a user-defined task.
      b. A tile is defined as the smallest unit of the system. Any tile consists of the following components:
           b.1. A CAN-Capable read-write PCB as the BusPlate.
           b.2. A casing consisting of the front case and the backplate
           b.3. Input and output elements as Light Emitting Diodes, Buttons, Switches and more mounted into the front plate of the casing
      c. A rack is defined as the structure carrying and spacing the tiles.
2. The basic structure for a rack is a 5mm wide frame with the inner sizing of 50x50mm and a thickness of minimum 4mm. By fusing such frames togoether a rack is built. Each basic frame resembles the size of one unit (1U).
3. We define three levels of controll elements protection to ensure a dynamic range of application and environemntal adaptation.
      a. A level 3 tile is defined as a tile with no switch protection against accidental action.
      b. A level 2 tile is defined as a tile with sufficient control elements protection to ensure protection against accidental action. Only fully contacted switches (e.g.       ON-ON) are allowed.
      c. A level 1 tile is defined as a tile with maximal protection against accidental action. Double action is the minimum requirement. We split the level 1 category in the following subgroups:
            c.1. A level 1-S tile is definied as a tile meeting the basic level 1 requirements and the additional requirement of the maxiaml control element density of one control element per rack unit.
            c.2. A level 1-HV tile is definied as a tile meeting the basic level 1 requirements and additionally having the front tile face colored in a high visiability pattern (e.g. black and yellow stripes, 15mm wide at a 45° angle to the bottom plate of the tile) and having a maxiaml control element density of one control element per rack unit.
```
The given standartization is applied to all the racks and tiles in this current project.

# Example solution
In the following secion I will present my solution for the standartization and problem.

## BusPlate
The core piece of the work is the BusPlate resembling a PCB with the following features:

- RP2040 controller
- USB-C connectivity
- CAN Bus feature with MCP2515 controller
- Power and data over RJ45
- Decentralized computing capability on board

The following pictures are the front and back of the BusPlate PCB.

<img src="https://github.com/mrk-fox/MHIPS/blob/main/pictures/BusPlate_F.png" style="width:auto;">
<img src="https://github.com/mrk-fox/MHIPS/blob/main/pictures/BusPlate.png" style="width:auto;">

The following picures are the single PCB layers in the order "Front, In 1, In 2, Back"

<img src="https://github.com/mrk-fox/MHIPS/blob/main/pictures/Front_PCB_Paths.png" style="width:auto;">
<img src="https://github.com/mrk-fox/MHIPS/blob/main/pictures/In1_PCB_Paths.png" style="width:auto;">
<img src="https://github.com/mrk-fox/MHIPS/blob/main/pictures/In2_PCB_Paths.png" style="width:auto;">
<img src="https://github.com/mrk-fox/MHIPS/blob/main/pictures/Back_PCB_Paths.png" style="width:auto;">
