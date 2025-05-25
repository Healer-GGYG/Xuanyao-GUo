# Xuanyao-GUO
🌈 Mood Pet 使用说明
Mood Pet 是一个情绪追踪互动程序，用户可以通过与不同的虚拟宠物互动来记录每日心情，参与小游戏提升情绪，还能可视化地查看情绪趋势。

🐾 启动方法
确保所有以下文件在同一目录下：
* main.py （Main program entry, handles user interaction ）
* pet.py （Defines pet attributes, personalities, and reactions） 
* emotion.py （Maps moods to scores and vice versa ）
* activity.py  （Contains all interactive games)
* logger.py (Handles CSV log creation, read, write )
* mood_visualizer.py (Generates mood trend bar charts)
* emotion_words.txt (Emotion word list used in word chain game)

终端中运行： python main.py



🎮 使用流程
Step 1：进入程序
* 程序启动后会提示你是否想要使用 Mood Pet。
* 输入 y 开始，输入 n 退出程序。
Step 2：选择宠物并命名
* 选择你喜欢的宠物类型（如狗狗、猫猫、龙等）。
* 给你的宠物取一个名字。
（宠物类型+宠物名字=user_id。作为用户查看历史数据的依据）
Step 3：输入当前心情
* 你需要从以下列表中输入一个当前心情（区分大小写不敏感）：
happy, excited, relaxed, neutral,
bored, tired, sad, stressed,
angry, anxious, frustrated, lonely
（如果选择这些情绪以外的词语系统会自动判定为neutral）
Step 4：宠物回应 + 活动推荐
* 你的宠物会基于性格和你的心情做出回应。（不同的宠物有不同的说话语气，并且会根据你当下的信息回应不同的信息）
* 它将推荐一项适合的小游戏，你可以：
    * 选择参与
    * 更换游戏
    * 退出游戏环节
Step 5：互动小游戏（任选其一）
* Guess the Number：猜数字，猜中提升情绪。
* Funny Quiz：趣味冷笑话问答，答对获得分数。
* Lucky Number：生成你的幸运数字。
* Lucky Colour：揭示你的幸运颜色。
* Emotional Word Chain：与宠物轮流说出情绪词接龙。
（每只宠物会玩以上2-3种游戏，不同的宠物会玩的游戏都是不一样的）
Step 6：情绪评分与记录
* 游戏互动后会计算并显示“综合心情评分”。
* 程序将询问是否记录今天的情绪日志，如今日已记录会提示是否覆盖。
Step 7：情绪趋势图（可选）
* 可选择查看过去 7、14、21 或 30 天的心情变化图表。

📊 情绪分数说明
用户心情会转换为数值（参见 emotion.py）：
得分越高，表示你今天情绪越积极。

📁 日志记录说明
程序会自动将记录保存至 mood_log.csv 文件，内容包括：
* 时间戳
* 用户 ID（宠物名 + 类型）
* 用户心情
* 情绪得分
你每天只能保存一次记录，除非选择覆盖。


