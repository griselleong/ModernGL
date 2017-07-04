import struct

import pygame
from pygame.locals import DOUBLEBUF, OPENGL

import ModernGL
from pyrr import Matrix44

width, height = 1280, 720

pygame.init()
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

ctx = ModernGL.create_context()

prog = ctx.program([
    ctx.vertex_shader('''
        #version 330

        uniform vec2 WindowSize;

        in vec2 in_vert;
        in vec3 in_color;

        out vec3 v_color;

        void main() {
            v_color = in_color;
            gl_Position = vec4(in_vert / WindowSize * 2.0, 0.0, 1.0);
        }
    '''),
    ctx.fragment_shader('''
        #version 330

        in vec3 v_color;
        out vec4 f_color;

        void main() {
            f_color = vec4(v_color, 1.0);
        }
    '''),
])

window_size = prog.uniforms['WindowSize']

vbo = ctx.buffer(struct.pack(
    '15f',
    0.0, 100.0, 1.0, 0.0, 0.0,
    -86.0, -50.0, 0.0, 1.0, 0.0,
    86.0, -50.0, 0.0, 0.0, 1.0,
))

vao = ctx.simple_vertex_array(prog, vbo, ['in_vert', 'in_color'])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ctx.viewport = (0, 0, width, height)
    ctx.clear(0.9, 0.9, 0.9)
    ctx.enable(ModernGL.BLEND)
    window_size.value = (width, height)
    vao.render()

    pygame.display.flip()
    pygame.time.wait(10)