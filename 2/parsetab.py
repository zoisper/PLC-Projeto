
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL COFF COM COMA CON FALSE IF INT LBRACE LCURLY MAIN NUM RBRACE RCURLY REAL SEMICOLON STRING TRUE VAR WHILEprogramm : MAIN LCURLY RCURLY'
    
_lr_action_items = {'MAIN':([0,],[2,]),'$end':([1,4,],[0,-1,]),'LCURLY':([2,],[3,]),'RCURLY':([3,],[4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programm':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programm","S'",1,None,None,None),
  ('programm -> MAIN LCURLY RCURLY','programm',3,'p_program','parser.py',9),
]
