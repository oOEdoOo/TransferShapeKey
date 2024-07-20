# TransferShapeKey.py 使用说明

TransferShapeKey.py 是一个用于在 Blender 中复制形状键的插件工具。
部分代码参考了youtube上的[视频]:(https://www.youtube.com/watch?v=Q13pBes8Wfc&t=31s)，同时也请教了ChatGPT。

## 安装

1. 下载 TransferShapeKey.py 文件。
2. 打开 Blender。
3. 进入 "Edit" -> "Preferences"。
4. 在 "Add-ons" 选项卡中，点击 "Install..." 按钮。
5. 选择下载的 TransferShapeKey.py 文件并点击 "Install Add-on"。
6. 启用插件，勾选 TransferShapeKey.py。

## 作用

1. 与Blender自带的Transfer ShapeKey按钮有点不同，本工具是将源对象的所有形状键复制到目标对象的同名形状键中。
2. 本工具不会检测源对象和目标对象的形状键是否一一对应，只会将源对象的形状键复制到目标对象的同名形状键中。
3. 本工具不会检测源对象和目标对象的顶点数是否一致（如果有检测需求，可将代码中的43、44、45行解开注释）。

## 使用

1. 工具位于Sidebar的Tool选项卡中，名字叫ShapeKeys Copy一栏下。
2. 选择要传递形状键的源对象和目标对象。
3. 点击 "Copy" 按钮。
4. 等待插件完成形状键的传递。
5. 检查目标对象的形状键是否已成功传递。

注意：在使用插件之前，请确保源对象和目标对象具有相同的拓扑结构。
