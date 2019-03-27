def fix_draw_figure(border, shape, style):
    print 'border=', border
    print 'shape=', shape
    print 'style=', style


dict1 = {'border': 4, 'shape': 'rectangle', 'style': 'dashed'}

fix_draw_figure(**dict1)
fix_draw_figure(6,'circle','solid')
fix_draw_figure(border=6, shape='circle', style='solid')
